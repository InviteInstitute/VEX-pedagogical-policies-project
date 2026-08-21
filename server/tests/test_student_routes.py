from unittest.mock import patch, MagicMock
from uuid import uuid4
import pytest

from src.routes.students import create_response, NO_RUNS_MESSAGE
from src.schemas import StudentResponseRequest
from src.feedback_policy import FeedbackClass


@patch("src.routes.students.sync_invite_hub_logs")
@patch("src.routes.students.fetch_events_from_db")
@patch("src.routes.students.generate_no_runs_llm_response")
@patch("src.routes.students.append_session_message")
@patch("src.routes.students.insert_message")
def test_create_response_zero_runs(
    mock_insert_message,
    mock_append_session,
    mock_no_runs_llm,
    mock_fetch_events,
    mock_sync_logs,
):
    # Setup: 0 runProject events in the database
    # Non-run event
    mock_event = MagicMock()
    mock_event.event_type = "blockChanged"
    mock_event.playground = "GO-Mars"
    mock_fetch_events.return_value = [mock_event]

    mock_no_runs_llm.return_value = {
        "response_text": "Please run your code once first to get help. Try checking the Pick Up a Sample project.",
        "model": "gpt-mock-model",
        "prompt": "mocked prompt",
    }

    payload = StudentResponseRequest(
        message_id="msg-123",
        session_id="20000000-0000-0000-0000-000000000001",
        playground="GO-Mars",
        student_message="I need help",
    )

    response = create_response(student_id="student-1", payload=payload)

    # Assertions
    expected_response = "Please run your code once first to get help. Try checking the Pick Up a Sample project."
    assert response.response_text == expected_response
    mock_append_session.assert_called_once_with(
        student_id="student-1",
        playground="GO-Mars",
        session_id=payload.session_id,
        role="assistant",
        content=expected_response,
    )
    mock_insert_message.assert_called_once()
    assert "current_stage" in mock_no_runs_llm.call_args.kwargs
    assert mock_no_runs_llm.call_args.kwargs["current_stage"].startswith("Stage 1:")
    assert "task" not in mock_no_runs_llm.call_args.kwargs
    assert "background_info" in mock_no_runs_llm.call_args.kwargs
    # Confirm sync was called
    mock_sync_logs.assert_called_once_with(student_id="student-1")


@patch("src.routes.students.sync_invite_hub_logs")
@patch("src.routes.students.fetch_events_from_db")
@patch("src.routes.students.select_current_playground_segment")
@patch("src.routes.students.has_active_project_run")
@patch("src.routes.students.compute_snapshot_for_student_session")
@patch("src.routes.students.determine_feedback_class")
@patch("src.routes.students.build_raw_logs_context")
@patch("src.routes.students.get_recent_session_messages")
@patch("src.routes.students.generate_robot_behavior_summary")
@patch("src.routes.students.generate_main_llm_response")
@patch("src.routes.students.append_session_message")
@patch("src.routes.students.insert_message")
def test_create_response_with_runs(
    mock_insert_message,
    mock_append_session,
    mock_llm_response,
    mock_robot_summary,
    mock_recent_messages,
    mock_raw_logs,
    mock_determine_feedback,
    mock_compute_snapshot,
    mock_has_active_run,
    mock_select_segment,
    mock_fetch_events,
    mock_sync_logs,
):
    # Setup: 1 runProject event and 1 other event
    run_event = MagicMock()
    run_event.event_type = "runProject"
    run_event.playground = "GO-Mars"

    other_event = MagicMock()
    other_event.event_type = "blockChanged"
    other_event.playground = "GO-Mars"

    mock_fetch_events.return_value = [run_event, other_event]
    mock_select_segment.return_value = ("GO-Mars", [run_event, other_event])
    mock_has_active_run.return_value = False
    
    mock_snapshot = MagicMock()
    mock_snapshot.to_dict.return_value = {}
    mock_compute_snapshot.return_value = mock_snapshot
    
    mock_determine_feedback.return_value = {FeedbackClass.ELABORATE}
    mock_raw_logs.return_value = "raw logs info"
    mock_recent_messages.return_value = []
    
    mock_robot_summary.return_value = {
        "response_text": "robot behaved well",
        "model": "gpt-mock-model",
        "prompt": "robot behavior prompt",
    }
    mock_llm_response.return_value = {
        "response_text": "Here is some helpful feedback",
        "model": "gpt-mock-model",
        "prompt": "main llm prompt",
    }

    payload = StudentResponseRequest(
        message_id="msg-123",
        session_id="20000000-0000-0000-0000-000000000001",
        playground="GO-Mars",
        student_message="I need help",
    )

    response = create_response(student_id="student-1", payload=payload)

    # Assertions
    assert response.response_text == "Here is some helpful feedback"
    # Verify determine_feedback_class was called with attempts=1
    mock_determine_feedback.assert_called_once_with(mock_snapshot, attempts=1)
    mock_append_session.assert_called_once_with(
        student_id="student-1",
        playground="GO-Mars",
        session_id=payload.session_id,
        role="assistant",
        content="Here is some helpful feedback",
    )
    mock_insert_message.assert_called_once()
    assert "current_stage" in mock_llm_response.call_args.kwargs
    assert mock_llm_response.call_args.kwargs["current_stage"].startswith("Stage 1:")
    assert "task" not in mock_llm_response.call_args.kwargs
    assert "background_info" in mock_llm_response.call_args.kwargs
    assert "current_stage" in mock_robot_summary.call_args.kwargs
    assert mock_robot_summary.call_args.kwargs["current_stage"].startswith("Stage 1:")
    assert "task" not in mock_robot_summary.call_args.kwargs
    assert "background_info" in mock_robot_summary.call_args.kwargs
