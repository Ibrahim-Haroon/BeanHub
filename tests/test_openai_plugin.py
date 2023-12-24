from scripts.openai_plugin import openai_api
import pytest
from mock import MagicMock, patch


@pytest.fixture
def mock_openai(mocker):
    return mocker.patch('scripts.openai_plugin.OpenAI')


def test_openai_api(mock_openai):
    # Arrange
    mock_completion = MagicMock()
    mock_completion.choices[0].message.content = "mocked_response"
    mock_openai.return_value.chat.completions.create.return_value = mock_completion

    # Act
    with patch('scripts.openai_plugin.OpenAI', return_value=mock_openai.return_value):
        result = openai_api(prompt="Test prompt", model_behavior="System message", api_key="foo_key")

    # Assert
    assert result == "mocked_response"
    mock_openai.return_value.chat.completions.create.assert_called_once_with(
        messages=[
            {"role": "system", "content": "System message"},
            {"role": "user", "content": "Test prompt"}
        ],
        model="gpt-3.5-turbo-1106"
    )
