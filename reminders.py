import re
import nlp_processing

reminders_qeue = []
def create_reminder(text):

    print("Creando recordatorio...")

    text = nlp_processing.reminders_preprocessing(text)
    text = text.replace("recordatorio", "").strip()
    text = re.sub(r'\bcre\w*', '', text)

    reminders_qeue.append(text)
    print("Recordatorio creado:", text)


def read_reminders():
    
    print("Recordatorios:", reminders_qeue)

