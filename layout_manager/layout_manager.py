"""Layout manager."""

# Because CustomTkinter has no stub file:
# pyright: reportUnknownMemberType = false
# pyright: reportMissingTypeStubs = false

import importlib
import pathlib
from typing import Any, Tuple

import customtkinter as ct


class LayoutManager:
    """Creates layouts."""

    def __init__(self) -> None:
        self._layouts: dict[str, Any] = {}
        self.import_layouts()

    def import_layouts(self) -> None:
        """Imports layouts."""

        _current_dir: pathlib.Path | None = None

        try:
            _current_dir = pathlib.Path(__file__).resolve().parent
            _file_names = [
                f.name
                for f in _current_dir.iterdir()
                if f.is_file() and f.suffix == ".py"
            ]

            # Dynamically import modules

            for _module_name in _file_names:
                full_module_name = (
                    f"layout_manager.{_module_name[:-3]}"  # Remove .py extension
                )
                _module = importlib.import_module(full_module_name)

                # If the module defines a register() function,
                # call it to register the search type.

                if hasattr(_module, "register"):
                    _name, _action = _module.register()
                    self._layouts[_name] = _action

        except FileNotFoundError:
            print(f"Directory '{_current_dir}' not found.")

    def create_layout(  # pylint: disable=too-many-arguments, too-many-positional-arguments
        self,
        master: ct.CTk | ct.CTkFrame,
        layout: str,
        padx: int | Tuple[int, int],
        pady: int | Tuple[int, int],
        gutter: int,
    ) -> Any:
        """Creates a layout with the specified parameters."""
        return self._layouts[layout](master, padx, pady, gutter)

    def list_layouts(self) -> None:
        """Lists the registered layouts."""
        for _layout in self._layouts.items():
            print(_layout)
