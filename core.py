import requests
from schedule_editor import Schedule

def start_chat():
    ask(
        "You are my personal assistant named Achilles, you keep me up to date on my schedule and let me know if i'm missing tasks and can help organize my schedule. You can help me add tasks/events, delete them, change them and suggest new ways to reorganize my schedule."
    )

def core():

    start_chat()
    
    user = input("You: ")
    response = ask(user)
    print("AI:", response)

def ask(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

schedule = Schedule("schedule.json")

while True:
    core()


