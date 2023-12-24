import pytest


def run_tests():
    result = pytest.main(['/openai_plugin/openai_api.py'])

    return result


if __name__ == "__main__":
    run_tests()
