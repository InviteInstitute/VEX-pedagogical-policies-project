STAGE_DESCRIPTIONS = {
    "default": "Help the student debug and improve their VEXcode VR program.",
    "GO-Mars": {
        1: """
## VEX VR Playground — Environment Description

### Coordinate System
The field uses a **2D top-down grid coordinate system**. The origin `(0, 0)` is at the **bottom-center** of the playfield (where the robot starts). **X increases to the right**, **Y increases upward**. Each grid cell is approximately **1 unit**.

---

### Robot (Agent)
- **Starting position:** `(0, 0)` — bottom-center of the field, inside the **green drop zone**.
- The robot faces **upward (north)** at spawn.
- The robot can **move, rotate, pick up boxes, and drop boxes**.

---

### Green Drop Zone (Goal Area)
- **Center:** `(0, 0)`
- **Bounds:** approximately `(-2, -2)` to `(2, 2)`
- This is where the robot **starts** and where **all boxes must be dropped**.

---

### Pickup Zones / Enclosures
There are **three enclosed arena sections** arranged in a cross/T-shape above the green zone. Each enclosure contains **colored boxes to be collected**.

#### Left Enclosure
- **Center:** `(-5, 4)`
- **Contents:** 2 **blue boxes**
  - Blue Box 1: `(-5.5, 4.5)`
  - Blue Box 2: `(-4.5, 3.5)`
- Surrounded by **brown/orange border walls**

#### Top-Center Enclosure
- **Center:** `(0, 8)`
- **Contents:** 2 **orange boxes**
  - Orange Box 1: `(-0.5, 8.5)`
  - Orange Box 2: `(0.5, 7.5)`
- Surrounded by **brown/orange border walls**

#### Right Enclosure
- **Center:** `(5, 4)`
- **Contents:** 2 **purple boxes**
  - Purple Box 1: `(4.5, 4.5)`
  - Purple Box 2: `(5.5, 3.5)`
- Surrounded by **brown/orange border walls**

---

### Scattered Orange Boxes (Open Field)
There are additional **loose orange boxes** placed in the open area of the field (not inside enclosures):
- Orange Loose Box 1: `(-7, 6)` (far left, near top-left corner)
- Orange Loose Box 2: `(-1, 8)` (near top-center enclosure entrance)

---

### Field Boundaries
- The playfield is a **white/gray dotted grid**.
- Approximate total field bounds: `(-8, -2)` to `(8, 10)`
- The orange surrounding color is **out-of-bounds**.

---

### Summary Table for LLM Inference

| Object | Color | Approx. Coordinates |
|---|---|---|
| Robot Start / Drop Zone | Green | `(0, 0)` |
| Blue Box 1 | Blue | `(-5.5, 4.5)` |
| Blue Box 2 | Blue | `(-4.5, 3.5)` |
| Orange Box 1 | Orange | `(-0.5, 8.5)` |
| Orange Box 2 | Orange | `(0.5, 7.5)` |
| Purple Box 1 | Purple | `(4.5, 4.5)` |
| Purple Box 2 | Purple | `(5.5, 3.5)` |
| Loose Orange Box 1 | Orange | `(-7, 6)` |
| Loose Orange Box 2 | Orange | `(-1, 8)` |

---
""",
        2: """
        ## VEX VR Playground — Textual Environment Description
---

### Coordinate System

- The playground uses a **grid-based coordinate system**.
- **Origin (0, 0)** is at the **bottom-center** of the map (where the robot starts, on the green tile).
- **X-axis** increases to the **right**, decreases to the **left**.
- **Y-axis** increases **upward** (north), decreases **downward** (south).
- Each **tile is approximately 1 unit × 1 unit**.
- The map is roughly **3 tiles wide × 7 tiles tall**, shaped like an **inverted T / cross**.

---

### Map Layout (Grid Zones)

| Zone Name | Tile Position (X, Y) | Description |
|---|---|---|
| **Start / Drop Zone** | (0, 0) | Green tile. Robot spawn point. This is the **goal/drop zone** for collected boxes. |
| **Central Corridor** | (0, 1) to (0, 4) | Narrow vertical corridor, 1 tile wide, connecting start zone to upper platform. |
| **Upper Platform** | (-1, 4) to (1, 6) | Wide 3-tile platform at the top. Contains multiple colored boxes. |
| **Left Wing** | (-1, 2) to (-1, 3) | Left branch off the central corridor. Contains a box cluster. |
| **Right Wing** | (1, 2) to (1, 3) | Right branch off the central corridor. Contains a single box. |

---

### Object Positions

| Object | Color | Approximate Position (X, Y) | Notes |
|---|---|---|---|
| **Box A** | Orange | (0, 6) | Top-center of upper platform, inside a dashed enclosure |
| **Box B** | Orange | (-1, 5) | Upper-left of platform, inside enclosure |
| **Box C** | Blue | (-1, 4) | Left side of upper platform |
| **Box D** | Purple | (1, 4) | Right side of upper platform, inside enclosure |
| **Box E** | Blue (large) | (-1, 2) | Left wing, prominent blue box |
| **Box F** | Purple/Multi** | (-1, 2) | Left wing, co-located with Box E cluster |
| **Robot** | — | (0, 0) | Starting on the green drop zone, facing north |
| **Drop Zone** | Green | (0, 0) | Target destination for all collected boxes |

---

### Navigation Rules (for LLM inference)

- The robot **must travel north** (increasing Y) from (0,0) through the corridor to reach the upper platform.
- **Left wing** is accessible by turning west (negative X) at approximately Y=2–3.
- **Right wing** is accessible by turning east (positive X) at approximately Y=2–3.
- **Upper platform** is accessible once Y ≥ 4; robot can move freely left/right there.
- After picking up a box, the robot **returns to (0, 0)** to drop it in the green zone.
- **Walls/boundaries** exist at the orange border tiles — the robot cannot cross them.

---

### Log Inference Tips for the Small LLM

- If log shows `position ~ (0, 0)` → robot is at **Start/Drop Zone**.
- If log shows `position ~ (0, 1–3)` → robot is in the **Central Corridor**.
- If log shows `position ~ (±1, 2–3)` → robot is in a **Wing Zone** (box cluster nearby).
- If log shows `position ~ (X, 4–6)` → robot is on the **Upper Platform** (multiple boxes present).
- `pickup event` at any position → box at that coordinate has been collected.
- `drop event` at `(0, 0)` → successful delivery to the green drop zone.

---
        """,
        3: """
        

## VEX VR Playground — Environment Description

### Coordinate System
- The playfield is a **grid-based map**, oriented **top-to-bottom vertically**.
- Assume the **origin (0, 0)** is at the **bottom-center** of the playfield (where the small white dot/robot starting marker appears).
- **X-axis** increases to the **right**, decreases to the **left**.
- **Y-axis** increases **upward** (north), decreases **downward** (south).
- Each visible tile is approximately **1 grid unit × 1 grid unit**.

---

### Layout (Top to Bottom, approximate grid coordinates)

| Object | Description | Approx. Coordinates (x, y) |
|---|---|---|
| **Top-left zone** | Orange-bordered tile with a small orange/white box (pickup item) | (-2, 6) |
| **Top-right zone** | Orange-bordered tile with a small orange/white box (pickup item) | (+2, 6) |
| **Mid-left zone** | Orange-bordered tile containing **blue boxes** (pickup items, stacked) | (-2, 4) |
| **Mid-right zone** | Orange-bordered tile containing a **purple box** (pickup item) | (+2, 4) |
| **Center-left obstacle** | Gray/white rectangular barrier (wall or static obstacle) | (-1, 3) |
| **Left cluster** | Group of colored boxes (orange, blue) — pickup items | (-2, 2) |
| **Green drop zone** | **Large green tile** — this is the **target drop zone** for collected boxes | (0, 1) |
| **Robot** | The VEX robot (player-controlled), currently positioned on the green drop zone | (0, 1) |
| **Red zone (bottom-left)** | Red tile with a vehicle/plane graphic — likely a **decorative or obstacle tile** | (-2, -1) |
| **Bottom-center** | Small white dot — likely **robot spawn/start point** | (0, -1) |
| **Bottom-right** | Tile with an **X/propeller graphic** — likely a **decorative or obstacle tile** | (+2, -1) |

---

### Key Rules for LLM Inference
1. **Pickup boxes** are located in **orange-bordered tiles** (top-left, top-right, mid-left, mid-right).
2. The **green tile** is the **only valid drop zone**. A successful drop is logged when the robot enters coordinates **(0, 1)** while carrying a box.
3. The **robot starts near (0, -1)** and must navigate upward (increasing Y) to reach boxes, then return to the green zone.
4. **Obstacles/walls** (gray barrier at approx. (-1, 3)) block direct paths — the robot must route around them.
5. Box colors serve as **identifiers**: blue ≈ mid-left zone, purple ≈ mid-right zone, orange ≈ top zones.

---
        """,
        4:"""
        # VEX VR Playground — Textual Environment Description

## Coordinate System
The environment uses a **2D top-down grid**. The origin `(0, 0)` is at the **bottom-left corner** of the playfield. The **X-axis** increases to the right, and the **Y-axis** increases upward. The full field spans approximately **200 units wide × 400 units tall** (2:4 aspect ratio based on the image).

---

## Field Layout

The field has a **T-shaped or cross-shaped corridor** structure with the following zones:

### Top Section — Upper Platform `(X: 0–200, Y: 280–400)`
A wide rectangular area divided into **two sub-platforms** (left and right), separated by a narrow orange gap in the center.

- **Top-Left Platform** `(X: 10–90, Y: 300–390)`
  - Contains a **pickup box cluster**: approximately 2–3 colored blocks (orange/blue) centered near `(50, 350)`
  - Decorative X-marker at top `(50, 380)`

- **Top-Right Platform** `(X: 110–190, Y: 300–390)`
  - Contains a **single large pickup box** (purple/blue) centered near `(150, 340)`
  - Decorative X-marker at top `(150, 380)`

---

### Middle Corridor — Narrow Vertical Passage `(X: 60–140, Y: 200–300)`
- A **narrow vertical hallway** connecting the top section to the lower section
- Contains a **horizontal barrier/wall segment** near `(100, 260)` — likely a checkpoint or gate object
- Passable by the robot; width approximately 80 units

---

### Lower Section — Main Arena `(X: 0–200, Y: 0–200)`
A wide open area subdivided into **four quadrant zones**:

| Quadrant | X Range | Y Range | Contents |
|---|---|---|---|
| **Bottom-Left** | 0–90 | 100–200 | Large orange/blue object cluster `(45, 155)` |
| **Bottom-Right (upper)** | 110–200 | 120–200 | Cylindrical object (gray/white barrel) `(160, 170)` |
| **Center** *(green drop zone)* | 60–140 | 100–180 | **🟩 Goal/Drop Zone** — green square `(100, 140)`, robot spawn ~`(100, 130)` |
| **Bottom-Left (lower)** | 0–90 | 0–100 | Red zone with large object `(40, 50)` |
| **Bottom-Right (lower)** | 110–200 | 0–100 | Orange zone with X-shaped object `(160, 40)` |

---

## Key Objects Summary

```
Object               | Type         | Approx. Coordinates
---------------------|--------------|---------------------
Pickup Box Cluster A | Collectible  | (50, 350)
Pickup Box B         | Collectible  | (150, 340)
Gate/Barrier         | Obstacle     | (100, 260)
Robot                | Agent        | (100, 130)
Green Drop Zone      | Goal         | (100, 145)
Barrel/Cylinder      | Obstacle     | (160, 170)
Red Zone Object      | Obstacle     | (40, 50)
X-Prop (lower right) | Decoration   | (160, 40)
```

---

## Inference Notes for LLM Log Parsing

When reading log data, a small LLM should apply these heuristics:

- **Y > 280** → robot is in the **upper collection zone** (near pickup boxes)
- **Y 200–280, X 60–140** → robot is **in the corridor**
- **X 60–140, Y 100–180** → robot is **at or near the drop zone**
- **Distance to `(100, 145)` < 15** → robot is **within drop zone**
- **Carrying = true + near green zone** → **drop action should trigger**
- Movement toward higher Y = moving **toward boxes**; lower Y = returning **to drop zone**
        """
    }
}


def resolve_stage_description(playground: str, stage: str | int | None) -> str:
    if stage is None:
        return STAGE_DESCRIPTIONS["default"]

    playground_dict = STAGE_DESCRIPTIONS.get(playground)
    if not isinstance(playground_dict, dict):
        return STAGE_DESCRIPTIONS["default"]

    if stage in playground_dict:
        return playground_dict[stage]

    try:
        int_stage = int(stage)
        if int_stage in playground_dict:
            return playground_dict[int_stage]
    except (ValueError, TypeError):
        pass

    try:
        str_stage = str(stage)
        if str_stage in playground_dict:
            return playground_dict[str_stage]
    except (ValueError, TypeError):
        pass

    return STAGE_DESCRIPTIONS["default"]