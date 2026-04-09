"""Các hàm kiểm tra dữ liệu dùng chung."""

from __future__ import annotations

import inspect
from typing import Any, Callable


class ValidationError(ValueError):
    """Lỗi kiểm tra dữ liệu đầu vào."""


def ensure_not_empty(value: str | None) -> bool:
    return value is not None and value.strip() != ""


def validate_menu_choice(choice: str, valid_choices: list[str]) -> bool:
    return choice in valid_choices


def find_callable(module: Any, candidates: list[str]) -> Callable | None:
    for name in candidates:
        fn = getattr(module, name, None)
        if callable(fn):
            return fn
    return None


def supports_argument(func: Callable, arg_name: str) -> bool:
    try:
        signature = inspect.signature(func)
    except (TypeError, ValueError):
        return False
    return arg_name in signature.parameters


def call_function(func: Callable, **kwargs: Any) -> Any:
    """Gọi hàm theo kwargs nhưng chỉ truyền những tham số mà hàm thực sự hỗ trợ."""
    signature = inspect.signature(func)
    accepted_kwargs = {
        key: value for key, value in kwargs.items() if key in signature.parameters and value is not None
    }
    return func(**accepted_kwargs)


def validate_key_with_module(module: Any, key: str, mode: str | None = None) -> None:
    validator = find_callable(module, ["validate_key", "is_valid_key", "check_key"])
    if validator is None:
        return

    result = call_function(validator, key=key, mode=mode)

    if isinstance(result, tuple) and len(result) == 2:
        ok, message = result
        if not ok:
            raise ValidationError(str(message))
        return

    if result is False:
        raise ValidationError("Key không hợp lệ theo kiểm tra của module.")


def normalize_exception_message(exc: Exception) -> str:
    message = str(exc).strip()
    return message or exc.__class__.__name__
