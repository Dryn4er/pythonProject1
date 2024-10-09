from typing import Any

import pytest

from src.decorators import log


def test_log(capsys: Any) -> Any:
    """Тест на работоспособность функции"""
    @log(filename="")
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    result = my_function(3, 5)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\nExecution time:0.0\n"
    assert result == 8


def test_log_error(capsys: Any) -> Any:
    """Тест на ошибки"""
    @log(filename="")
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    captured = capsys.readouterr()
    with pytest.raises(TypeError):
        my_function(3, "5")
        assert captured.err == 'my_function error: TypeError. Inputs: (3, "5"), {}'
