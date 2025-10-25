"""Test program for layout manager."""

# Because CustomTkinter has no stub file:
# pyright: reportUnknownMemberType = false
# pyright: reportMissingTypeStubs = false

import customtkinter as ct

from layout_manager import LayoutManager

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

LAYOUT = "layout_09"
GEOM = "800x600"


class LayoutTest(ct.CTk):
    """LayoutTest."""

    def __init__(
        self,
    ):
        super().__init__()

        # Configure main frame.

        self.title(LAYOUT)
        self.geometry(GEOM)

        self.attributes("-topmost", True)
        self.resizable(True, False)

        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        # Choose a layout, create it and add to current frame.

        self._layout_manager: LayoutManager = LayoutManager()

        self._layout = self._layout_manager.create_layout(
            self, layout=LAYOUT, padx=10, pady=10, gutter=5
        )
        self._layout.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

    def start_gui(self) -> None:
        """Starts the mainloop to run the gui."""
        self.mainloop()


def main():
    """Main app function."""
    _layout_test: LayoutTest = LayoutTest()
    _layout_test.mainloop()


if __name__ == "__main__":
    main()
