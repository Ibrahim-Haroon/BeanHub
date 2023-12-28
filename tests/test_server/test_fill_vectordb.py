import pytest
from unittest.mock import patch, MagicMock, mock_open
from scripts.server.fill_vectordb import fill_database
import pandas as pd
from os import path


@pytest.fixture
def mock_components(mocker):
    return {
        'openai_embedding_api': mocker.patch('scripts.server.fill_vectordb.openai_embedding_api'),
        'connection_string': mocker.patch('scripts.server.connection_string.connection_string'),
        'register_vector': mocker.patch('pgvector.psycopg2.register_vector'),
        'connect': mocker.patch('scripts.server.fill_vectordb.psycopg2.connect'),
        'input': mocker.patch('builtins.input'),
    }


@pytest.fixture
def mock_boto3_session_client(mocker):
    return mocker.patch('boto3.session.Session.client', return_value=MagicMock())


@pytest.fixture
def mock_aws_info_csv(mocker):
    # Mock the read_csv function to return a sample DataFrame without reading the actual file
    secret_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "aws-info.csv")

    # Use patch to mock the open function and create a mock file
    with patch('builtins.open', new_callable=mock_open,
               read_data='secret_name,region_name,aws_access_key_id,aws_secret_access_key\ntest_secret,us-east-1,aws_access_key_id,aws_secret_access_key\n'):
        # Patch pandas.read_csv to return a DataFrame
        mocker.patch('pandas.read_csv', return_value=pd.DataFrame({
            'secret_name': ['test_secret'],
            'region_name': ['us-east-1'],
            'aws_access_key_id': ['aws_access_key_id'],
            'aws_secret_access_key': ['aws_secret_access_key']
        }))

        mocker.patch('os.path.join', return_value=secret_file_path)

        yield secret_file_path



@pytest.fixture
def mock_database_info_csv(mocker):
    # Mock the read_csv function to return a sample DataFrame without reading the actual file
    data_base_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "database-info.csv")

    # Use patch to mock the open function and create a mock file
    with patch('builtins.open', new_callable=mock_open,
               read_data='dbname,user,password,host,port\ndbname,user,password,host,port\n'):
        # Patch pandas.read_csv to return a DataFrame
        mocker.patch('pandas.read_csv', return_value=pd.DataFrame({
            'dbname': ['dbname'],
            'user': ['user'],
            'password': ['password'],
            'host': ['host'],
            'port': ['port']
        }))

        mocker.patch('os.path.join', return_value=data_base_file_path)

        yield data_base_file_path


@patch('builtins.input', side_effect=["YES", "beanKnowsWhatBeanWants"])
def test_fill_database_success(mocker, mock_components, mock_aws_info_csv, mock_database_info_csv, mock_boto3_session_client):
    # Arrange
    data = [{"MenuItem": {"itemName": "TestItem", "price": 10.0}}]
    key = "mock_api_key"

    # Act
    result = fill_database(data, key)

    # Assert
    assert result is True


@patch('builtins.input', side_effect=["YES", "wrong_passkey"])
def test_fill_database_exits_when_wrong_passkey_given(mock_components):
    # Arrange
    data = [{"MenuItem": {"itemName": "Item1", "price": 10.0}}]
    key = "your_key_here"

    # Act
    result = fill_database(data, key)

    # Assert
    assert result is False


@patch('builtins.input', return_value="NO")
def test_fill_database_exits_when_no_entered(mock_components):
    # Arrange
    data = [{"MenuItem": {"itemName": "Test", "price": 0.0}}]
    key = "mock_key"

    # Act
    result = fill_database(data, key)

    # Assert
    assert result is False