from scripts.audio_recorder import record_until_silence

script_path = 'scripts.audio_recorder'


def test_record_until_silence_function_returns_none_when_no_audio():
    # Arrange
    expected_transcription = None

    # Act
    audio_data, transcribed_audio = record_until_silence()

    # Assert
    assert transcribed_audio == expected_transcription
