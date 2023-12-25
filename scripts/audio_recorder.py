import speech_recognition as speech
from pydub import AudioSegment


def record_until_silence():
    recognizer = speech.Recognizer()
    with speech.Microphone() as source:
        print("Recording... Speak until you want to stop.")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        audio_data = []
        transcribed_audio = None

        while True:
            try:
                audio_chunk = recognizer.listen(source, timeout=2)
                audio_data.append(audio_chunk.frame_data)

                # Try to convert speech to text
                transcribed_audio = recognizer.recognize_google(audio_chunk)
                print(f"Recognized: {transcribed_audio}")

            except speech.WaitTimeoutError:
                print("Timeout. No speech detected.")
                break
            except speech.UnknownValueError:
                print("Could not understand audio.")
            except speech.RequestError as e:
                print(f"Google Speech Recognition request failed: {e}")

        return b"".join(audio_data), transcribed_audio


def save_as_mp3(audio_data, output_filename="recorded_audio.mp3"):
    audio_segment = AudioSegment(audio_data, sample_width=2, frame_rate=44100, channels=1)
    audio_segment.export(output_filename, format="mp3")
    print(f"Audio saved as {output_filename}")


if __name__ == "__main__":
    recorded_audio, _ = record_until_silence()
    save_as_mp3(recorded_audio)
