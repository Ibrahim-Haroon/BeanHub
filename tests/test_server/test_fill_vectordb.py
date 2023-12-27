import pandas as pd
import pytest
from unittest.mock import patch, MagicMock, mock_open
from scripts.server.fill_vectordb import fill_database
from os import path


@pytest.fixture
def mock_components(mocker):
    # Mocking the 'get_secret' function from 'script_path.aws_secret'
    aws_secret_mock = mocker.patch('scripts.server.aws_secret.get_secret')

    mock_api_key_data = 'your_mock_api_key_here'
    mocker.patch('builtins.open', mock_open(read_data=mock_api_key_data), create=True)

    # Mock the secret_file_path
    secret_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "aws-info.csv")
    api_key_file_path = key_file_path = path.join(path.dirname(path.realpath(__file__)), "../../other/" + "api_key")

    # Mock the 'api_key' attribute or function in the 'other' module
    api_key_mock = mocker.patch('other.api_key', return_value='mock_api_key')

    # Mocking file operations and other components...
    with patch('builtins.open', mock_open(read_data='...')):
        mocker.patch('pandas.read_csv', return_value=pd.DataFrame({...}))
        mocker.patch('os.path.exists', return_value=True)
        mocker.patch('os.path.join', return_value=secret_file_path)
        mocker.path('os.path.join', return_value=api_key_file_path)

        return {
            'api_key': api_key_mock,
            'openai_embedding_api': mocker.patch('scripts.server.fill_vectordb.openai_embedding_api'),
            'connection_string': mocker.patch('script_path.connection_string.connection_string'),
            'register_vector': mocker.patch('pgvector.psycopg2.register_vector'),
            'connect': mocker.patch('psycopg2.connect'),
            'get_secret': aws_secret_mock,
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
