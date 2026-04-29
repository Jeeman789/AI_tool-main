import requests
from schedule_editor import Schedule

def start_chat():
    try:
        ask(
            "You are my personal assistant named Achilles, you keep me up to date on my schedule and let me know if i'm missing tasks and can help organize my schedule. You can help me add tasks/events, delete them, change them and suggest new ways to reorganize my schedule."
        )
    except:
        print("This did not work")

def chat():
    
    print("Llama is ready, type \"leave\" to exit session\n")

    start_chat()

    while True:
        user = input("You: ")
        if user == "leave":
            break
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

def main():
    schedule = Schedule("schedule.json")

    while True:
        print("\n#####==== MENU ====####")
        print("1. Chat with Achilles")
        print("2. Edit Schedule")
        print("3. Quit")
        print("####==== MENU ====####\n")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            chat()
        elif choice == "2":
            schedule.list_tasks()
        elif choice == "3":
            print("\nSee ya!")
            break
        else:
            print("\ninvalid entry, try again")

if __name__ == "__main__":
    main()


