import boto3
import pandas as pd
from os import path
from aiohttp import ClientError


def get_secret() -> str:
    """
    @purpose: validate Amazon SDK
    @rtype: str
    @return: secret response
    """
    secret_file_path = connection_string_file_path = path.join(path.dirname(path.realpath(__file__)), "../..", "other", "aws-info.csv")

    df = pd.read_csv(secret_file_path)
    row = df.iloc[0]

    secret_name = row['secret_name']
    region_name = row['region_name']
    aws_access_key_id = row['aws_access_key_id']
    aws_secret_access_key = row['aws_secret_access_key']

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    return get_secret_value_response['SecretString']
