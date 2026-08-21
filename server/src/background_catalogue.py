BACKGROUND_DESCRIPTIONS = {
    "default": "",
    "GO-Mars": {
        "common_spec": """KNOWLEDGE BASE: VEX GO - MARS MATH EXPEDITION (VEXCODE VR)
1. Environment and Robot Specifications
Platform: VEXcode VR (Virtual Robotics)
Robot Model: Virtual Competition Advanced Hero Robot (pre-configured in the Toolbox)
Drivetrain and Gyro Sensor: Controlled via standard Drivetrain code blocks and equipped with an integrated Gyro Sensor for precise turns. Heading reports values from 0 to 359.9 degrees, where clockwise rotation is positive.
Arm Mechanism: Controlled by the Arm Motor on Port 2. The default starting position is lowered at 0 degrees, and its range of motion spans from 0 degrees (lowest) to 420 degrees (highest). Continuous motion uses the [Spin] block, while specific positioning uses [Spin to position].
Front Eye Sensor: Located on the front of the robot between the arm forks when the arm is lowered. It reports object presence (found an object?), color detection (detects red/blue/green?), brightness percentage (0% to 100%), and hue values (0 to 359 degrees).""",
        
        "common_ui": """3. VEXcode VR Playground Features and UI
Default Stage: Opening the playground defaults to Stage 1.
Changing Stages: Select the Expand button in the top-left corner of the Playground Window, click the Location icon, and choose Stage 1, 2, 3, or 4.
Playground Snapshot Download: Located in the expanded top-left menu (Download icon). It downloads a .png image of the Playground showing final robot/object positions, remaining time, and final score.""",
        
        1: {
            "gameplay": """2. Gameplay Stages and Scoring Rules
Stage 1: Crater and Rover
Task: Remove a sample from a crater.
Task: Move the Rover out of the crater.
Rule: An object is considered "out" of the crater when no part of it is touching the inside crater walls or the crater floor.
Standard Match Duration: 1 minute (01:00).
Point Value: Each completed task is worth 1 point.""",
            "ui_extra": "",
            "examples": """4. INSTRUCTIONS FOR AI: Using Example Projects to Guide Students
Direct students to starter code: Tell the student they can access pre-built starter code in VEXcode VR by navigating to File -> Open Examples.
Recommend the correct project for their specific stage or task:
- If working on Stage 1 (Crater tasks): Direct them to the Pick Up a Sample example project to see how to remove a sample from a crater.
Enforce the Stage Selection Rule: Always remind the student that after loading an Example Project, they must manually open the Playground menu and select the correct Stage (1, 2, 3, or 4) so the field matches the code.
Guide their learning process: Do not just give them answers. Tell them to run the example project first to observe the robot's behavior, then change one block or number at a time to see how it affects the robot.""",
            "nasa": """5. INSTRUCTIONS FOR AI: Using NASA Mars 2020 Mission Context
Make real-world STEM connections:
- Crater Samples & Lab Delivery: Explain that the Perseverance rover collects geological samples on Mars and stores them via depot caching so future missions can retrieve them and bring them to Earth.
Engage and motivate: Use this background to congratulate students when they complete a task by connecting their programming success to the work of real NASA engineers."""
        },
        
        2: {
            "gameplay": """2. Gameplay Stages and Scoring Rules
Stage 1: Crater and Rover (Active)
- Task: Remove a sample from a crater.
- Task: Move the Rover out of the crater.
Stage 2: Lab Scoring (Active)
- Task: Move a sample to the Lab Tile.
- Task: Place a sample on top of the Lab.
- Task: Place a sample onto its matching colored square on top of the Lab.
Rule: An object is considered "out" of the crater when no part of it is touching the inside crater walls or the crater floor.
Rule: Placing samples on the Lab roof requires lifting the arm up to 420 degrees.
Rule: Color matching requires aligning the sample color to the corresponding colored square on the roof.
Standard Match Duration: 1 minute (01:00).
Point Value: Each completed task is worth 1 point.""",
            "ui_extra": "",
            "examples": """4. INSTRUCTIONS FOR AI: Using Example Projects to Guide Students
Direct students to starter code: Tell the student they can access pre-built starter code in VEXcode VR by navigating to File -> Open Examples.
Recommend the correct project for their specific stage or task:
- If working on Stage 1 (Crater tasks): Direct them to the Pick Up a Sample example project to see how to remove a sample from a crater.
- If working on Stage 2 (Lab tasks): Direct them to the Moving Samples example project to see a 3-point routine that removes a sample from a crater, moves it to the Lab Tile, and places it on top of the Lab.
Enforce the Stage Selection Rule: Always remind the student that after loading an Example Project, they must manually open the Playground menu and select the correct Stage (1, 2, 3, or 4) so the field matches the code.
Guide their learning process: Do not just give them answers. Tell them to run the example project first to observe the robot's behavior, then change one block or number at a time to see how it affects the robot.""",
            "nasa": """5. INSTRUCTIONS FOR AI: Using NASA Mars 2020 Mission Context
Make real-world STEM connections:
- Crater Samples & Lab Delivery: Explain that the Perseverance rover collects geological samples on Mars and stores them via depot caching so future missions can retrieve them and bring them to Earth.
Engage and motivate: Use this background to congratulate students when they complete a task by connecting their programming success to the work of real NASA engineers."""
        },
        
        3: {
            "gameplay": """2. Gameplay Stages and Scoring Rules
Stage 1: Crater and Rover (Active)
- Task: Remove a sample from a crater.
- Task: Move the Rover out of the crater.
Stage 2: Lab Scoring (Active)
- Task: Move a sample to the Lab Tile.
- Task: Place a sample on top of the Lab.
- Task: Place a sample onto its matching colored square on top of the Lab.
Stage 3: Solar Panel, Landing Site, and Rocket (Active)
- Task: Tilt the Solar Panel down.
- Task: Clear debris from the Landing Site.
- Task: Place the Helicopter on the Landing Site.
- Task: Lift the Rocket Ship upright.
- Task: End the match with the Robot touching the Red Tile.
Rule: An object is considered "out" of the crater when no part of it is touching the inside crater walls or the crater floor.
Rule: Placing samples on the Lab roof requires lifting the arm up to 420 degrees.
Rule: Color matching requires aligning the sample color to the corresponding colored square on the roof.
Rule: The Landing Site is considered "clear" when no debris touches the orange landing site in the center of the Tile.
Rule: Helicopter placement is scored via an interactive UI button once the debris is cleared.
Rule: For Red Tile contact, any part of the robot touching any part of the Red Tile at the end of the match counts.
Standard Match Duration: 1 minute (01:00).
Point Value: Each completed task is worth 1 point.""",
            "ui_extra": "The Helicopter Button (Stages 3 and 4): Located in the lower-right corner of the Playground Window. It appears grayed out and unclickable while debris remains on the Landing Site. It automatically enables once all debris is pushed off the orange Landing Site. Clicking the active button drops the virtual Helicopter onto the Landing Site to score the point.",
            "examples": """4. INSTRUCTIONS FOR AI: Using Example Projects to Guide Students
Direct students to starter code: Tell the student they can access pre-built starter code in VEXcode VR by navigating to File -> Open Examples.
Recommend the correct project for their specific stage or task:
- If working on Stage 1 (Crater tasks): Direct them to the Pick Up a Sample example project to see how to remove a sample from a crater.
- If working on Stage 2 (Lab tasks): Direct them to the Moving Samples example project to see a 3-point routine that removes a sample from a crater, moves it to the Lab Tile, and places it on top of the Lab.
- If working on Stage 3 (Solar Panel or Landing Site): Direct them to the Tilt the Solar Panel example project for arm positioning, or the Clear the Landing Site example project to see how to drive across the stage and push debris away.
Enforce the Stage Selection Rule: Always remind the student that after loading an Example Project, they must manually open the Playground menu and select the correct Stage (1, 2, 3, or 4) so the field matches the code.
Guide their learning process: Do not just give them answers. Tell them to run the example project first to observe the robot's behavior, then change one block or number at a time to see how it affects the robot.""",
            "nasa": """5. INSTRUCTIONS FOR AI: Using NASA Mars 2020 Mission Context
Make real-world STEM connections:
- Crater Samples & Lab Delivery: Explain that the Perseverance rover collects geological samples on Mars and stores them via depot caching so future missions can retrieve them and bring them to Earth.
- Tilting the Solar Panel: Explain that solar panels must be properly positioned and maintained to supply solar energy and keep surface equipment powered.
- Clearing the Landing Site: Explain that the NASA Mars Helicopter, Ingenuity, rode to Mars on the belly of the Perseverance rover and requires a clear, debris-free zone to safely take off and land during experimental flights.
Engage and motivate: Use this background to congratulate students when they complete a task by connecting their programming success to the work of real NASA engineers."""
        },
        
        4: {
            "gameplay": """2. Gameplay Stages and Scoring Rules
Stage 1: Crater and Rover (Active)
- Task: Remove a sample from a crater.
- Task: Move the Rover out of the crater.
Stage 2: Lab Scoring (Active)
- Task: Move a sample to the Lab Tile.
- Task: Place a sample on top of the Lab.
- Task: Place a sample onto its matching colored square on top of the Lab.
Stage 3: Solar Panel, Landing Site, and Rocket (Active)
- Task: Tilt the Solar Panel down.
- Task: Clear debris from the Landing Site.
- Task: Place the Helicopter on the Landing Site.
- Task: Lift the Rocket Ship upright.
- Task: End the match with the Robot touching the Red Tile.
Stage 4: Fuel Cell Scoring (Active)
- Task: Remove a fuel cell from its cradle.
- Task: Move a fuel cell to the Rocket Ship.
- Task: Move a fuel cell to the Landing Site.
Rule: An object is considered "out" of the crater when no part of it is touching the inside crater walls or the crater floor.
Rule: Placing samples on the Lab roof requires lifting the arm up to 420 degrees.
Rule: Color matching requires aligning the sample color to the corresponding colored square on the roof.
Rule: The Landing Site is considered "clear" when no debris touches the orange landing site in the center of the Tile.
Rule: Helicopter placement is scored via an interactive UI button once the debris is cleared.
Rule: For Red Tile contact, any part of the robot touching any part of the Red Tile at the end of the match counts.
Rule: All field elements are active, requiring students to strategize their pathing to maximize points within the 1-minute match limit.
Standard Match Duration: 1 minute (01:00).
Point Value: Each completed task is worth 1 point.""",
            "ui_extra": "The Helicopter Button (Stages 3 and 4): Located in the lower-right corner of the Playground Window. It appears grayed out and unclickable while debris remains on the Landing Site. It automatically enables once all debris is pushed off the orange Landing Site. Clicking the active button drops the virtual Helicopter onto the Landing Site to score the point.",
            "examples": """4. INSTRUCTIONS FOR AI: Using Example Projects to Guide Students
Direct students to starter code: Tell the student they can access pre-built starter code in VEXcode VR by navigating to File -> Open Examples.
Recommend the correct project for their specific stage or task:
- If working on Stage 1 (Crater tasks): Direct them to the Pick Up a Sample example project to see how to remove a sample from a crater.
- If working on Stage 2 (Lab tasks): Direct them to the Moving Samples example project to see a 3-point routine that removes a sample from a crater, moves it to the Lab Tile, and places it on top of the Lab.
- If working on Stage 3 (Solar Panel or Landing Site): Direct them to the Tilt the Solar Panel example project for arm positioning, or the Clear the Landing Site example project to see how to drive across the stage and push debris away.
- If working on Stage 4 (Fuel Cells): Direct them to the Scoring with Fuel Cells example project to see how to remove a Fuel Cell from its cradle and move it to the Rocket Ship.
Enforce the Stage Selection Rule: Always remind the student that after loading an Example Project, they must manually open the Playground menu and select the correct Stage (1, 2, 3, or 4) so the field matches the code.
Guide their learning process: Do not just give them answers. Tell them to run the example project first to observe the robot's behavior, then change one block or number at a time to see how it affects the robot.""",
            "nasa": """5. INSTRUCTIONS FOR AI: Using NASA Mars 2020 Mission Context
Make real-world STEM connections:
- Crater Samples & Lab Delivery: Explain that the Perseverance rover collects geological samples on Mars and stores them via depot caching so future missions can retrieve them and bring them to Earth.
- Tilting the Solar Panel: Explain that solar panels must be properly positioned and maintained to supply solar energy and keep surface equipment powered.
- Clearing the Landing Site: Explain that the NASA Mars Helicopter, Ingenuity, rode to Mars on the belly of the Perseverance rover and requires a clear, debris-free zone to safely take off and land during experimental flights.
- Rocket Ship & Fuel Cells: Explain that while Perseverance will remain on Mars, future Earth-return missions will require rocket ships and alternative chemical power sources—like fuel cells—to launch samples back to Earth.
Engage and motivate: Use this background to congratulate students when they complete a task by connecting their programming success to the work of real NASA engineers."""
        }
    }
}


def resolve_background_description(playground: str, stage: int | str | None = None) -> str:
    entry = BACKGROUND_DESCRIPTIONS.get(playground)
    if not entry:
        return BACKGROUND_DESCRIPTIONS["default"]

    if not isinstance(entry, dict):
        return entry

    # It's a stage-separated dictionary (like GO-Mars)
    # Default to stage 4 if none specified or not found
    resolved_stage = 4
    if stage is not None:
        try:
            resolved_stage = int(stage)
        except (ValueError, TypeError):
            pass
    if resolved_stage not in entry:
        resolved_stage = 4

    stage_data = entry[resolved_stage]
    common_spec = entry.get("common_spec", "")
    common_ui = entry.get("common_ui", "")
    
    gameplay = stage_data.get("gameplay", "")
    ui_extra = stage_data.get("ui_extra", "")
    examples = stage_data.get("examples", "")
    nasa = stage_data.get("nasa", "")

    # Construct the final description string
    parts = []
    if common_spec:
        parts.append(common_spec)
    if gameplay:
        parts.append(gameplay)
    
    # Merge common ui and stage specific ui extras
    ui_part = common_ui
    if ui_extra:
        ui_part = f"{ui_part}\n{ui_extra}"
    if ui_part:
        parts.append(ui_part)
        
    if examples:
        parts.append(examples)
    if nasa:
        parts.append(nasa)

    return "\n\n".join(parts)
