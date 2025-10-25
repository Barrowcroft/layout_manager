"""Layout manager."""

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


class LayoutManager:  # pylint: disable=too-few-public-methods
    """Creates layouts."""

    def __init__(self) -> None:
        self._layouts: dict[str, Layout] = {}
        self._layouts["layout_00"] = Layout00
        self._layouts["layout_01"] = Layout01
        self._layouts["layout_02"] = Layout02
        self._layouts["layout_03"] = Layout03
        self._layouts["layout_04"] = Layout04
        self._layouts["layout_05"] = Layout05
        self._layouts["layout_06"] = Layout06
        self._layouts["layout_07"] = Layout07
        self._layouts["layout_08"] = Layout08
        self._layouts["layout_09"] = Layout09

    def create_layout(  # pylint: disable=too-many-arguments, too-many-positional-arguments
        self,
        master: ct.CTk | ct.CTkFrame,
        layout: str,
        padx: int | Tuple[int, int],
        pady: int | Tuple[int, int],
        gutter: int,
    ) -> ReturnType:
        """creates a layout with the specified parameters."""
        return self._layouts[layout](master, padx, pady, gutter)
