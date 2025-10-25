# A layout manager for customtkinter.

Rather than spending time doing boiler plate code to create frame layouts 
this class will create a number of basic layouts.

# Installation

`pip install git+ssh://git@github.com/Barrowcroft/layout_manager.git`

or

`uv add git+https://git@github.com/barrowcroft/layout_manager.git`

# Usage

Choose a layout, create it and add to current frame.

```
from layout_manager import LayoutManager

self._layout_manager: LayoutManager = LayoutManager()

self._layout = self._layout_manager.create_layout(
    self, layout="layout_00", padx=10, pady=10, gutter=5
)

self._layout.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
```

The created frames are simply named as: left, middle, right, top, bottom.

# Example layouts

layout_01
![Example](scr_01.png)
layout_02
![Example](scr_02.png)
layout_03
![Example](scr_03.png)
layout_04
![Example](scr_04.png)
layout_05
![Example](scr_05.png)
layout_06
![Example](scr_06.png)
layout_07
![Example](scr_07.png)
layout_08
![Example](scr_08.png)
layout_09
![Example](scr_09.png)