import requests
from schedule_editor import Schedule

def start_chat():
    ask(
        "You are my personal assistant named Albus"
    )

def core():
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
schedule.create_schedule_file()

while True:
    core()


