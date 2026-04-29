import json
from pathlib import Path

class Schedule:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_schedule()

    def create_schedule_file(self):
        with open(self.filename, 'w') as f:
            base = {
                "Monday": [],
                "Tuesday": [],
                "Wednesday": [],
                "Thursday": [],
                "Friday": [],
                "Saturday": [],
                "Sunday": []
            }
            json.dump(base, f)

        return base
    
    def clear_file(self):
        with open(self.filename, "w"):
            pass

    def add_task(self, day, task, time):
        return self.tasks[day].append[task, time]
    
    def add_task(self, day, task, time):
        return self.tasks[day].append[task, time]
    
    def load_schedule(self):
        data = None
        if not Path(self.filename).exists():
            data = self.create_schedule_file()
        else:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

                if not all(item in data for item in days):
                    self.clear_file()
                    data = self.create_schedule_file()
        return data
                

    def save_schedule(self):
        with open(self.filename, "w"):
            json.dump(self.tasks)

    def list_tasks(self):
        print("\nMonday: ", self.tasks["Monday"])
        print("Tuesday: ", self.tasks["Tuesday"])
        print("Wednesday: ", self.tasks["Wednesday"])
        print("Thursday: ", self.tasks["Thursday"])
        print("Friday: ", self.tasks["Friday"])
        print("Saturday: ", self.tasks["Saturday"])
        print("Sunday: ", self.tasks["Sunday"])
    