import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
from scripts.server.similarity_search import similarity_search
from scripts.server.connection_string import connection_string


@pytest.fixture
def mock_nlp_bard():
    with patch('scripts.ai_integration.nlp_bard') as mock:
        yield mock

@pytest.fixture
def mock_openai_embedding_api():
    with patch('scripts.ai_integration.openai_embedding_api') as mock:
        yield mock

@pytest.fixture
def mock_get_secret():
    #Finish Writing where get_secret is
    with patch('scripts.get_secret') as mock:
        yield mock

@pytest.fixture
def mock_connect():
    with patch('pgvector.psycopg2.connect') as mock:
        yield mock

def test_similarity_search(mock_nlp_bard, mock_openai_embedding_api, mock_get_secret, mock_connect):
    # Mocking necessary functions and objects
    mock_cursor = MagicMock()
    mock_connection = MagicMock()
    mock_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor
    mock_nlp_bard.return_value = "formatted_string"
    mock_openai_embedding_api.return_value = "fake_embedding"

    # Input parameters
    order = "dummy"
    key = "fake_key"
    aws_csv_file = StringIO("fake_aws_csv")
    database_csv_file = StringIO("fake_db_csv")

    # Call the function
    result = similarity_search(order, key, aws_csv_file, database_csv_file)

    # Assertions
    mock_nlp_bard.assert_called_once_with(order)
    mock_openai_embedding_api.assert_called_once_with("formatted_string", key)
    mock_get_secret.assert_called_once_with(aws_csv_file)
    mock_connect.assert_called_once_with(connection_string(database_csv_file))
    mock_cursor.execute.assert_called_once_with(""" SELECTED id, item_name, price, embeddings
                FROM products
                ORDER BY embeddings <-> %s limit 3;""",
            ("fake_embedding",))
    mock_cursor.fetchall.assert_called_once()
    assert result == mock_cursor.fetchall.return_value
