import pandas as pd
import pytest
from unittest.mock import patch, MagicMock, mock_open
from scripts.server.fill_vectordb import fill_database
from os import path


@pytest.fixture
def mock_components(mocker):
    return {
        'openai_embedding_api': mocker.patch('scripts.server.fill_vectordb.openai_embedding_api'),
        'connection_string': mocker.patch('script_path.connection_string.connection_string'),
        'register_vector': mocker.patch('pgvector.psycopg2.register_vector'),
        'connect': mocker.patch('psycopg2.connect'),
        'input': mocker.patch('builtins.input'),
    }


@patch('builtins.input', return_value="NO")
def test_fill_database_input_red_no(mock_components):
    # Arrange
    data = [{"MenuItem": {"itemName": "Test", "price": 0.0}}]
    key = "mock_key"

    # Act
    result = fill_database(data, key)

    # Assert
    assert result is False


@patch('builtins.input', side_effect=["YES", "wrong_passkey"])
def test_fill_database_wrong_passkey(mock_components):
    # Arrange
    data = [{"MenuItem": {"itemName": "Item1", "price": 10.0}}]
    key = "your_key_here"

    # Act
    result = fill_database(data, key)

    # Assert
    assert result is False
