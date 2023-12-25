from scripts.audio_recorder import record_until_silence
from os import path

script_path = 'scripts.audio_recorder'


def test_record_until_silence_with_empty_audio_file():
    audio_file_path = path.join(path.dirname(path.realpath(__file__)), "empty_audio.wav")
    # audio_file = AudioSegment.from_file(audio_file_path, format="wav")

    expected_transcription = None

    _, actual_transcription = record_until_silence(audio_file_path)

    assert expected_transcription == actual_transcription



def test_record_until_silence_with_non_empty_audio_file():
    # Arrange
    audio_file_path = path.join(path.dirname(path.realpath(__file__)), "test_audio.wav")
    # audio_file = AudioSegment.from_file(audio_file_path, format="wav")

    expected_transcription = "this is a test"

    _, actual_transcription = record_until_silence(audio_file_path)

    assert expected_transcription == actual_transcription

