import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
from scripts.server.similarity_search import similarity_search
from scripts.server.connection_string import connection_string

@pytest.fixture
def mock_components(mocker):
    return {
        'nlp_bard': mocker.patch('scripts.ai_integration.nlp_bard'),
        'openai_embedding_api': mocker.patch('scripts.server.fill_vectordb.openai_embedding_api'),
        'connection_string': mocker.patch('scripts.server.connection_string.connection_string'),
        'register_vector': mocker.patch('pgvector.psycopg2.register_vector'),
        'connect': mocker.patch('scripts.server.fill_vectordb.psycopg2.connect'),
        'input': mocker.patch('builtins.input'),
    }


def test_similarity_search(mocker):
    # Mocking necessary functions and objects
    mock_cursor = MagicMock()
    mock_connection = MagicMock()
    mocker.mock_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor
    mocker.mock_nlp_bard.return_value = "formatted_string"
    mocker.mock_openai_embedding_api.return_value = "fake_embedding"

    # Input parameters
    order = "dummy"
    key = "fake_key"
    aws_csv_file = StringIO("fake_aws_csv")
    database_csv_file = StringIO("fake_db_csv")

    # Call the function
    result = similarity_search(order, key, aws_csv_file, database_csv_file)

    # Assertions
    mocker.mock_nlp_bard.assert_called_once_with(order)
    mocker.mock_openai_embedding_api.assert_called_once_with("formatted_string", key)
    mocker.mock_get_secret.assert_called_once_with(aws_csv_file)
    mocker.mock_connect.assert_called_once_with(connection_string(database_csv_file))
    mock_cursor.execute.assert_called_once_with(""" SELECTED id, item_name, price, embeddings
                FROM products
                ORDER BY embeddings <-> %s limit 3;""",
            ("fake_embedding",))
    mock_cursor.fetchall.assert_called_once()
    assert result == mock_cursor.fetchall.return_value
