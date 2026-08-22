
---
# 🔷 Grid-based Pattern Generator - V3.7 🔷
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
  - apply current pattern configuration to a set of patterns
  - import and export the full collection as JSON
- Grid and filling controls
  - set grid size by columns and rows
  - set type of grid : orthogonal or isometric
  - clear the current canvas or reset the grid
  - fill the grid automatically following custom rules (see [Grid filling options](#-custom-grid-filling-options))
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
  - show or hide the shapes
  - show or hide drawn lines
  - crop exports to the active grid area
  - add an index marker with selectable positions (left, centred, right, edge)
- Transformations ** NEW **
  - enhance pattern creation by using scaling, shifting and symmetry
  - see [Transformations](#-transformations--new-)
- Export options
  - export the current pattern as SVG
  - batch export the full collection to SVG files
- Multilingual UI
  - English and French interface support

---
# ⌨️ Keyboard shortcuts
General:
- `Ctrl+A`: add a new pattern
- `Ctrl+D`: duplicate the current pattern
- `Ctrl+R`: rename the current pattern
- `Ctrl+Delete`: delete the current pattern

Within the pattern list:
- `F2`: rename the selected pattern
- `Delete` / `Backspace`: delete the selected
- `Shift+Up`: move the selected pattern up
- `Shift+Down`: move the selected pattern down
- `Ctrl+click`: add pattern to the selection

---
# 🔬 Detailed features

## 🔁 Transformations ** NEW **
The tool supports a couple of pattern transformation\
There are four type of transformation:
- *scale*: redimension the pattern by muliplying or dividing the grid size following one or two axis
- *shift*: shift the complete pattern of custom steps following one or two axis
- *copy & shift*: copy the pattern and shift it of one grid size in one or two dimension
- *symmetry*: perform axial symmetry of the pattern following one or two axis

**_Note_**: Transformation can be applied to several pattern at once by selecting multiple pattern in the pattern list before clicking on the transformation button.

## 🔳 Custom grid filling options
The tool supports an autofill feature to place shapes on nodes following custom rules.\
There are three type of node:
- *free*: node unoccupied by a line or a dot
- *occupied*: node already occupied by a line or a dot
- *loop*: node included into a loop formed by lines and/or dots

For any type of node, the filling option could be configured to:
- *void*: leave or make empty the node
- *plain*: add a plain shape on the node
- *outlined*: add an outlined shape on the node

**_Note_**: Grid filling can be applied to several pattern at once with or witout copying current pattern filling rules by selecting multiple pattern in the pattern list before clicking on the fill button.

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

## ⏬ Mass operations
The tool allow a couple of mass operation to speed-up collection editing.

To enable the mass operations, select mutliple pattern in the list of the collection panel using either:
-  `Ctrl + click` to add pattern to the selection <br>
or 
- `click` on the first pattern and `click` on the last pattern while holding `Shift` key.

The mass operations available are:
- apply the current pattern configuration (grid, tool and parameters settings)
- fill the grid with current pattern configuration or with each individual pattern filling rules
- apply a transformation

## 📤 SVG file generation
SVG files generation is WYSIWYG ("What You See Is What You get") based except for the grid.\
If the grid is displayed, the primary file does not include the grid and a second SVG file including the grid is generated with the `_grid` suffix.