import pytest
from unittest.mock import patch, MagicMock
from scripts.server.fill_vectordb import fill_database


@pytest.fixture
def mock_api_key():
    with patch('other.api_key') as mock:
        yield mock


@pytest.fixture
def mock_openai_embedding_api():
    with patch('scripts.server.fill_vectordb.openai_embedding_api') as mock:
        yield mock


@pytest.fixture
def mock_connection_string():
    with patch('scripts.server.connection_string.connection_string') as mock:
        yield mock


@pytest.fixture
def mock_register_vector():
    with patch('pgvector.psycopg2.register_vector') as mock:
        yield mock


@pytest.fixture
def mock_connect():
    with patch('psycopg2.connect') as mock:
        yield mock


@pytest.fixture
def mock_get_secret():
    with patch('scripts.server.aws_secret.get_secret') as mock:
        mock.return_value = {
            'secret_name': 'secret_name',
            'region_name': 'region_name',
            'aws_access_key_id': 'aws_access_key_id',
            'aws_secret_access_key': 'aws_secret_access_key'
        }
        yield mock


@pytest.fixture
def mock_input():
    with patch('builtins.input') as mock:
        yield mock


@patch('builtins.input', side_effect=["YES", "beanKnowsWhatBeanWants"])
def test_fill_database_success(mock_api_key, mock_openai_embedding_api, mock_connection_string,
                               mock_register_vector, mock_connect, mock_get_secret, mock_input):
    # Arrange
    data = [{"MenuItem": {"itemName": "Test", "price": 0.0}}]
    key = "mock_key"

    # Act
    result = fill_database(data, key)

    # Assert
    assert result is True


@patch('builtins.input', return_value="NO")
def test_fill_database_input_red_no(mock_input):
    # Arrange
    data = [{"MenuItem": {"itemName": "Test", "price": 0.0}}]
    key = "mock_key"

    # Act
    result = fill_database(data, key)

    # Assert
    assert result is False


@patch('builtins.input', side_effect=["YES", "wrong_passkey"])
def test_fill_database_wrong_passkey(mock_input):
    # Arrange
    data = [{"MenuItem": {"itemName": "Item1", "price": 10.0}}]
    key = "your_key_here"

    # Act
    result = fill_database(data, key)

    # Assert
    assert result is False
