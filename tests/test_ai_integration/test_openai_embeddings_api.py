from scripts.ai_integration.openai_embeddings_api import *
import pytest
from mock import MagicMock, patch
from typing import Final


script_path: Final[str] = 'scripts.ai_integration.openai_embeddings_api'


@pytest.fixture
def mock_openai(mocker):
    return mocker.patch(script_path + '.OpenAIEmbeddings')


def test_openai_embeddings_api(mock_openai_embeddings):
    # Arrange
    expected_embeddings_instance = MagicMock()
    mock_openai_embeddings.return_value = expected_embeddings_instance
    expected_vectors = [1, 2]
    expected_embeddings_instance.embed_query.side_effect = expected_vectors

    # Act
    result_vectors, result_embeddings = openai_embedding_api(texts=["text1", "text2"], api_key="foo_key")

    # Assert
    assert result_vectors == expected_vectors
    assert result_embeddings == expected_embeddings_instance
    mock_openai_embeddings.assert_called_once_with(api_key="foo_key")



def test_parse_menu_csv(mocker):
    # Arrange
    expected_output = [
        "{'MenuItem': {'itemName': 'test', 'price': 0.0}}",
    ]
    mocker.patch('pandas.read_csv', return_value=pd.DataFrame({"item_name": ["test"], "price": [0.0]}))

    # Act
    result = parse_menu_csv()

    # Assert
    assert result == expected_output
