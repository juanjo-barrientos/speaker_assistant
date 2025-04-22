import re
import reminders

def regex_preprocessing(text_steammed,text):
    
    # Remove special characters and numbers
    text_steammed = re.sub(r'[^a-zA-Z\s]', '', text_steammed)

    # Funcion de recordatorios
    pattern_one = r"\bcre\b.*\brecordatori\w*\b|\bestablec\b.*\brecordatori\w*\b"
    
    if re.search(pattern_one, text_steammed):

        reminders.create_reminder(text)

    pattern_two = "\blis\b.*\brecordatori\w*\b|\bmostr\b.*\brecordatori\w*\b"

    if re.search(pattern_two, text_steammed):
        print("Listando recordatorios...")
        reminders.read_reminders()
    
    return text_steammed