# pylint: skip-file

"""Layout manager stub file."""

# Because CustomTkinter has no stub file:
# pyright: reportUnknownMemberType = false
# pyright: reportMissingTypeStubs = false

from typing import Any, Tuple

import customtkinter as ct

class LayoutManager:
    """Creates layouts."""

    _layouts: dict[str, Any]

    def __init__(self) -> None: ...
    def import_layouts(self) -> None: ...
    def create_layout(
        self,
        master: ct.CTk | ct.CTkFrame,
        layout: str,
        padx: int | Tuple[int, int],
        pady: int | Tuple[int, int],
        gutter: int,
    ) -> Any: ...
    def list_layouts(self) -> None: ...
