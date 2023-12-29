import pytest
from mock import patch, MagicMock
from io import StringIO
import csv
from scripts.server.similarity_search import similarity_search


@pytest.fixture
def mock_components(mocker):
    return {
        'nlp_bard': mocker.patch('scripts.ai_integration.nlp_bard'),
        'openai_embedding_api': mocker.patch('scripts.server.similarity_search.openai_embedding_api'),
        'connection_string': mocker.patch('scripts.server.connection_string.connection_string'),
        'connect': mocker.patch('scripts.server.similarity_search.psycopg2.connect'),
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


def test_similarity_search_returns_true_when_given_valid_params(mocker, mock_boto3_session_client, mock_components):
    # Arrange
    data = str({"input": {"Test"}})
    key = "mock_api_key"
    database_info = [
        ["dbname", "user", "password", "host", "port"],
        ["mydb", "myuser", "mypassword", "localhost", "port"]]
    aws_info = [
        ["secret_name", "region_name", "aws_access_key_id", "aws_secret_access_key"],
        ["name", "us-east-1", "aws_access_key_id", "aws_secret_access_key"]]

    aws = as_csv_file(aws_info)
    db = as_csv_file(database_info)

    _, res = similarity_search(data, key=key, aws_csv_file=aws, database_csv_file=db)

    assert res is True, f"expected search to be successful but {res}"
