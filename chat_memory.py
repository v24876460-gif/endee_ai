chat_history = []

def add(role,text):
    chat_history.append((role,text))

def history():
    return chat_history