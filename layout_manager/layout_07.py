"""Layout 07"""

from typing import Tuple

import customtkinter as ct

# Because CustomTkinter has no stub file:
# pyright: reportUnknownMemberType = false
# pyright: reportMissingTypeStubs = false

TOP = 30
BOTTOM = 30
LEFT = 200


class Layout07(ct.CTkFrame):  # pylint: disable=too-many-ancestors
    """Layout 07"""

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

        self.rowconfigure(index=0, weight=0)
        self.rowconfigure(index=1, weight=1)
        self.rowconfigure(index=2, weight=0)
        self.columnconfigure(index=0, weight=0)
        self.columnconfigure(index=1, weight=1)

        self.top: ct.CTkFrame = ct.CTkFrame(self, height=TOP)
        self.top.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=self._padx,
            pady=(self._pady[0], gutter),
            sticky="nswe",
        )

        self.left: ct.CTkFrame = ct.CTkFrame(self, width=LEFT)
        self.left.grid(
            row=1,
            column=0,
            padx=(self._padx[0], gutter),
            pady=(0, gutter),
            sticky="nswe",
        )

        self.right: ct.CTkFrame = ct.CTkFrame(self)
        self.right.grid(
            row=1, column=1, padx=(0, self._padx[1]), pady=(0, gutter), sticky="nswe"
        )

        self.bottom: ct.CTkFrame = ct.CTkFrame(self, height=BOTTOM)
        self.bottom.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=self._padx,
            pady=(0, self._pady[1]),
            sticky="nswe",
        )
