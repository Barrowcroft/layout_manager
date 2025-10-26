"""Layout 02"""

from typing import Tuple

import customtkinter as ct

# Because CustomTkinter has no stub file:
# pyright: reportUnknownMemberType = false
# pyright: reportMissingTypeStubs = false

RIGHT = 200


def register() -> Tuple[str, ct.CTkFrame]:
    """Registers the layout."""
    return ("layout_02", Layout02)  # type: ignore


class Layout02(ct.CTkFrame):  # pylint: disable=too-many-ancestors
    """Layout 02"""

    def __init__(
        self,
        master: ct.CTk | ct.CTkFrame,
        padx: int | Tuple[int, int],
        pady: int | Tuple[int, int],
        gutter: int | None = 5,
    ) -> None:
        super().__init__(master)

        # Save padding and gutter values.

        if isinstance(padx, int):
            self._padx = (padx, padx)
        else:
            self._padx = padx

        if isinstance(pady, int):
            self._pady = (pady, pady)
        else:
            self._pady = pady

        self._gutter: int | None = gutter

        # Layout frames.

        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=0)

        self.left: ct.CTkFrame = ct.CTkFrame(self)
        self.left.grid(
            row=0,
            column=0,
            padx=(self._padx[0], gutter),
            pady=self._pady,
            sticky="nswe",
        )

        self.right: ct.CTkFrame = ct.CTkFrame(self, width=RIGHT)
        self.right.grid(
            row=0,
            column=1,
            padx=(0, self._padx[1]),
            pady=self._pady,
            sticky="nswe",
        )
