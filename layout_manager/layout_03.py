"""Layout 03"""

from typing import Tuple

import customtkinter as ct

# Because CustomTkinter has no stub file:
# pyright: reportUnknownMemberType = false
# pyright: reportMissingTypeStubs = false

LEFT = 200
RIGHT = 200


def register() -> Tuple[str, ct.CTkFrame]:
    """Registers the layout."""
    return ("layout_03", Layout03)  # type: ignore


class Layout03(ct.CTkFrame):  # pylint: disable=too-many-ancestors
    """Layout 03"""

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
        self.columnconfigure(index=0, weight=0)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=0)

        self.left: ct.CTkFrame = ct.CTkFrame(self, width=LEFT)
        self.left.grid(
            row=0,
            column=0,
            padx=(self._padx[0], gutter),
            pady=self._pady,
            sticky="nswe",
        )

        self.middle: ct.CTkFrame = ct.CTkFrame(self)
        self.middle.grid(
            row=0,
            column=1,
            padx=(0, gutter),
            pady=self._pady,
            sticky="nswe",
        )

        self.right: ct.CTkFrame = ct.CTkFrame(self, width=RIGHT)
        self.right.grid(
            row=0,
            column=2,
            padx=(0, self._padx[1]),
            pady=self._pady,
            sticky="nswe",
        )
