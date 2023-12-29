import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
import csv
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

@pytest.fixture()
def mock_boto3_session_client(mocker):
    return mocker.patch('boto3.session.Session.client', return_value=MagicMock())


def as_csv_file(data: [[str]]) -> StringIO:
    file_object = StringIO()
    writer = csv.writer(file_object)
    writer.writerows(data)
    file_object.seek(0)

    return file_object


def test_similarity_search(mocker):

    assert 1 == 1
