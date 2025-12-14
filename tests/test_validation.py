import pytest
import sys
import os

# Garantir que o diretório do projeto esteja no path para importar Testes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Testes import validate_inputs


def test_empty_fields():
    ok, msg, age = validate_inputs("", "", "")
    assert not ok
    assert "preencha" in msg


def test_invalid_age_nonint():
    ok, msg, age = validate_inputs("João", "abc", "Masculino")
    assert not ok
    assert "idade" in msg.lower() or "válida" in msg.lower()


def test_invalid_age_negative():
    ok, msg, age = validate_inputs("João", "-5", "Masculino")
    assert not ok


def test_invalid_age_zero():
    ok, msg, age = validate_inputs("João", "0", "Masculino")
    assert not ok


def test_unselected_sex():
    ok, msg, age = validate_inputs("João", "30", "Selecione")
    assert not ok


def test_valid_inputs():
    ok, msg, age = validate_inputs("João", "30", "Masculino")
    assert ok
    assert msg is None
    assert age == 30
