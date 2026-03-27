
---
# 🔷 Grid-based Pattern Generator 🔷
---

This tool generates SVG files from patterns made of shapes and lines placed on a grid.


---
# 🚀 Getting started

1. This script uses only the Python standard library. No external packages are required.
    - Python 3.10+ (Developed and tested on 3.14)
    - Tkinter (included by default in most Python installations)
1. Clone the repository or download `main.py`.
1. Run: `python main.py`
1. Start creating your patterns:
    - Use the left panel to manage patterns and collections.
    - Use the central controls to configure grid size, fill options, shape tools, and export settings.
    - Click the canvas to place shapes or draw lines.

---
# ✴ Key Features

- Pattern collection management
  - create, rename, copy, delete and reorder patterns
  - rename the current collection
  - import and export the full collection as JSON
- Grid and filling controls
  - set grid size by columns and rows
  - clear the current canvas or reset the grid
  - fill the grid automatically following predefined rules (see [Grid filling options](#grid-filling-options))
- Shape drawing tools
  - place circle or square shapes at grid nodes
  - toggle between outlined and filled shapes
  - choose shape color, size, and outline width
- Line drawing tools
  - draw and remove line segments between grid nodes
  - block nodes to prevent shape placement
  - adjust line thickness and line color
- Display options
  - show or hide the grid
  - show or hide drawn lines
  - crop exports to the active grid area
  - add an index marker with selectable positions (left, centred, right, edge)
- Export options
  - export the current pattern as SVG
  - batch export the full collection to SVG files
- Multilingual UI
  - English and French interface support

---
# 🔬 Detailed features

## 🔳 Grid filling options
The tool supports an autofill feature to place shapes on nodes that are not occupied by a line or a dot.
There are three filling rules currently available:
- A: fill empty cells with loop detection
    - all unoccupied nodes are filled with the selected shape
    - nodes enclosed by lines are filled with outlined/hollow shapes if enabled
- B: fill empty cells without loop detection
    - all unoccupied nodes are filled with the selected shape
- C: fill all cells or outline occupied cells depending on mode
    - if outlined shapes are disabled, this behaves like option B
    - otherwise, all nodes of the grid are filled with the selected shape:
        - unoccupied nodes with full/plain shapes
        - occupied nodes with outlined/hollow shapes

## ⚒ Tool usage
### 🔵 Shape tool
With the shape tool selected:
- to **add a full/plain shape**, click on an unoccupied node
- to **add a outlined/hollow shape**, click on a full shape with the outlined mode enabled
- to **remove a shape**, click on an outlined/hollow shape or on a full/plain shape with the outlined mode disabled


### ✒️ Drawing tool
With the drawing tool selected:
- to **draw a line**, click on one node and then click on another node
- to **delete a line**, click on both endpoints of an existing line
- to **add a dot**, click on the same node twice
- to **remove a dot**, click on an existing dot

## 📤 SVG file generation
Several SVG files may be generated depending on the selected export options.

The primary SVG file contains the pattern drawn to fit a complete shape on the grid boundary.

If the pattern contains shapes, the export does not include drawn lines by default.

If the pattern contains only drawn lines, the export includes the line drawing.

When the crop option is selected, an extra SVG file is generated with the `_cropped` suffix and contains the pattern cropped to the grid boundary.

When both the grid and the lines are displayed, an extra SVG file is generated with the `_full` suffix and contains the shapes, lines, and grid, optionally cropped.