from scripts.audio_recorder import record_until_silence
import speech_recognition as speech
from mock import MagicMock, patch
from pydub import AudioSegment

script_path = 'scripts.audio_recorder'


def test_record_until_silence_with_empty_audio_file():
    audio_file_path = '/Users/ibrahimharoon/Python/BeanHub/tests/empty_audio.wav'
    # audio_file = AudioSegment.from_file(audio_file_path, format="wav")

    expected_transcription = None

    _, actual_transcription = record_until_silence(audio_file_path)

    assert expected_transcription == actual_transcription



def test_record_until_silence_with_non_empty_audio_file():
    # Arrange
    audio_file_path = '/Users/ibrahimharoon/Python/BeanHub/tests/test_audio.wav'
    # audio_file = AudioSegment.from_file(audio_file_path, format="wav")

    expected_transcription = "this is a test"

    _, actual_transcription = record_until_silence(audio_file_path)

    assert expected_transcription == actual_transcription

