# pylint: skip-file

"""Layout manager stub file."""

# Because CustomTkinter has no stub file:
# pyright: reportUnknownMemberType = false
# pyright: reportMissingTypeStubs = false

from typing import Tuple, Type

import customtkinter as ct

from layout_manager import (
    Layout00,
    Layout01,
    Layout02,
    Layout03,
    Layout04,
    Layout05,
    Layout06,
    Layout07,
    Layout08,
    Layout09,
)

Layout = (
    Type[Layout00]
    | Type[Layout01]
    | Type[Layout02]
    | Type[Layout03]
    | Type[Layout04]
    | Type[Layout05]
    | Type[Layout06]
    | Type[Layout07]
    | Type[Layout08]
    | Type[Layout09]
)
ReturnType = (
    Layout00
    | Layout01
    | Layout02
    | Layout03
    | Layout04
    | Layout05
    | Layout06
    | Layout07
    | Layout08
    | Layout09
)

class LayoutManager:
    """Creates layouts."""

    _layouts: dict[str, Layout]

    def __init__(self) -> None: ...
    def create_layout(
        self,
        master: ct.CTk | ct.CTkFrame,
        layout: str,
        padx: int | Tuple[int, int],
        pady: int | Tuple[int, int],
        gutter: int,
    ) -> ReturnType: ...
