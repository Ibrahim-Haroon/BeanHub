import pytest
from mock import mock_open, mock, patch
import boto3
from aiohttp import ClientError
from scripts.server.aws_secret import get_secret
import pandas as pd
from os import path


# Define a fixture for mocking pandas.read_csv
@pytest.fixture
def mock_pandas_read_csv(mocker):
    # Mock the read_csv function to return a sample DataFrame without reading the actual file
    secret_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "aws-info.csv")

    # Use patch to mock the open function and create a mock file
    with patch('builtins.open', new_callable=mock_open,
               read_data='secret_name,region_name,aws_access_key_id,aws_secret_access_key\ntest_secret,us-east-1,test_access_key,test_secret_key\n'):
        # Patch pandas.read_csv to return a DataFrame
        mocker.patch('pandas.read_csv', return_value=pd.DataFrame({
            'secret_name': ['test_secret'],
            'region_name': ['us-east-1'],
            'aws_access_key_id': ['test_access_key'],
            'aws_secret_access_key': ['test_secret_key']
        }))

        mocker.patch('os.path.join', return_value=secret_file_path)

        yield secret_file_path


# Define a fixture for mocking boto3.session.Session.client
@pytest.fixture
def mock_boto3_session_client(mocker):
    return mocker.patch('boto3.session.Session.client', return_value=mock.MagicMock())


# Define a fixture for mocking boto3.client.get_secret_value
@pytest.fixture
def mock_boto3_get_secret_value():
    with patch('scripts.server.aws_secret.boto3.client') as mock_client:
        mock_secret_value = {'SecretString': '{"key": "value"}'}
        mock_client.return_value.get_secret_value.return_value = mock_secret_value
        yield mock_client, mock_secret_value


# Test the get_secret function
def test_get_secret(mock_pandas_read_csv, mock_boto3_session_client, mock_boto3_get_secret_value):
    # Arrange
    mock_client, expected_result = mock_boto3_get_secret_value

    # Act
    result = get_secret()

    # Assert
    mock_boto3_session_client.assert_called_once_with(
        service_name='secretsmanager',
        region_name='us-east-1',
        aws_access_key_id='test_access_key',
        aws_secret_access_key='test_secret_key'
    )

