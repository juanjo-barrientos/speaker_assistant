import re
import reminders

patterns = [r"\bcre\b.*\brecordatori\w*\b|\bestablec\b.*\brecordatori\w*\b",
             r"\blist\b.*\brecordatori\w*\b|\bmo\bmuestr*\brecordatori\w*\b",]

functions = [reminders.create_reminder, reminders.read_reminders]


def regex_preprocessing(text_steammed,text):
    
    for pattern in patterns:
        match = re.search(pattern, text_steammed)
        if match:
            index = patterns.index(pattern)
            function = functions[index]
            function(text)
            
    
    return text_steammed