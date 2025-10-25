# pylint: skip-file

"""Stub file for Layout 05"""

# Because CustomTkinter has no stub file:
# pyright: reportUnknownMemberType = false
# pyright: reportMissingTypeStubs = false

from typing import Tuple, Union

import customtkinter as ct

class Layout05(ct.CTkFrame):
    """Layout 05"""

    _padx: Tuple[int, int]
    _pady: Tuple[int, int]
    _gutter: Union[int, None]
    main: ct.CTkFrame

    def __init__(
        self,
        master: Union[ct.CTk, ct.CTkFrame],
        padx: Union[int, Tuple[int, int]],
        pady: Union[int, Tuple[int, int]],
        gutter: Union[int, None] = 5,
    ) -> None: ...
