import pytest

from src.decorators import log


def test_log(capsys):
    @log(filename='')
    def my_function(x, y):
        return x + y

    result = my_function(3, 5)
    captured = capsys.readouterr()
    assert captured.out == 'my_function ok\nExecution time:0.0\n'
    assert result == 8


def test_log_error(capsys):
    @log(filename='')

    def my_function(x, y):
        return x + y

    captured = capsys.readouterr()
    with pytest.raises(TypeError):
        assert captured.err == 'my_function error: TypeError. Inputs: (3, "5"), {}'
