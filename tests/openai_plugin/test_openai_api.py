import os
import sys
import pytest

# Add the path to the root of your project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from openai_plugin.openai_api import OpenAPI


@pytest.fixture
def openapi_instance():
    return OpenAPI(api_key="your_api_key")


def test_openai_caller_with_model_behavior(openapi_instance):
    # Arrange
    prompt = "Test prompt"
    model_behavior = "Test behavior"

    with patch("your_module.OpenAI", MagicMock) as mock_openai:
        mock_client = mock_openai.return_value
        mock_completion = MagicMock()
        mock_client.chat.completions.create.return_value = mock_completion
        mock_completion.choices[0].message.content = "Mocked response"

        # Act
        result = openapi_instance.openai_caller(prompt, model_behavior)

        # Assert
        assert mock_openai.call_count == 1
        mock_client.chat.completions.create.assert_called_once_with(
            messages=[
                {"role": "system", "content": model_behavior},
                {"role": "user", "content": prompt}
            ],
            model="gpt-3.5-turbo-1106"
        )
        assert result == "Mocked response"


def test_openai_caller_without_model_behavior(openapi_instance):
    # Arrange
    prompt = "Test prompt"

    # Mock the OpenAI API call using MagicMock
    with patch("your_module.OpenAI", MagicMock) as mock_openai:
        mock_client = mock_openai.return_value
        mock_completion = MagicMock()
        mock_client.chat.completions.create.return_value = mock_completion
        mock_completion.choices[0].message.content = "Mocked response"

        # Act
        result = openapi_instance.openai_caller(prompt)

        # Assert
        assert mock_openai.call_count == 1
        mock_client.chat.completions.create.assert_called_once_with(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-3.5-turbo-1106"
        )
        assert result == "Mocked response"
