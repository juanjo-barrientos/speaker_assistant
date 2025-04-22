import pyaudio
import json
from vosk import Model, KaldiRecognizer

from nlp_processing import text_preprocessing
from regex_processing import regex_preprocessing

# Carga el modelo de voz en español
model = Model("./vosk-model-small-es-0.42")

# Inicializa PyAudio y el reconocedor
recognizer = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()

# Configura el micrófono
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8000)
stream.start_stream()

print("Escuchando...")

try:
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            if text:
                print("USUARIO: ", text)
                processing = " ".join(text_preprocessing(text))
                regex_process = regex_preprocessing(processing, text)

                
except KeyboardInterrupt:
    print("Interrumpido por el usuario")

stream.stop_stream()
stream.close()
p.terminate()
