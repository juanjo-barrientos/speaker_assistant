import re
import nlp_processing
from speaker import Speaker

spk = Speaker()

reminders_qeue = []
def create_reminder(text):

    print("Creando recordatorio...")

    text = nlp_processing.reminders_preprocessing(text)
    text = text.replace("recordatorio", "").strip()
    text = re.sub(r'\bcre\w*', '', text)
    text = re.sub(r'\bestablec\w*', '', text)

    reminders_qeue.append(text)

    spk.speak("Recordatorio creado: " + text)


def read_reminders(text):
    
    spk.speak("Recordatorios:")
    for reminder in reminders_qeue:
        spk.speak(reminder)

