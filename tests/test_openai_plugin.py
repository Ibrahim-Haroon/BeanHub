from scripts.openai_plugin import openai_api
import pytest
from unittest.mock import MagicMock, patch


@pytest.fixture
def mock_openai(mocker):
    return mocker.patch('scripts.openai_plugin.OpenAI')


def test_openai_api(mock_openai):
    # Create a MagicMock for the API response
    mock_completion = MagicMock()
    mock_completion.choices[0].message.content = "mocked_response"
    mock_openai.return_value.chat.completions.create.return_value = mock_completion

    # Call the function with some input
    with patch('scripts.openai_plugin.OpenAI', return_value=mock_openai.return_value):
        result = openai_api(prompt="Test prompt", model_behavior="System message", api_key="foo_key")

    # Assert that the function returns the expected result
    assert result == "mocked_response"

    # Assert that the API call was made with the correct parameters
    mock_openai.return_value.chat.completions.create.assert_called_once_with(
        messages=[
            {"role": "system", "content": "System message"},
            {"role": "user", "content": "Test prompt"}
        ],
        model="gpt-3.5-turbo-1106"
    )
