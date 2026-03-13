import json
from pathlib import Path

class Schedule:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.create_schedule_file()

    def create_schedule_file(self):
        if not Path(self.filename).exists():
            with open(self.filename, 'w') as f:
                json.dump({"Schedule": {
                    "Monday": [],
                    "Tuesday": [],
                    "Wednesday": [],
                    "Thursday": [],
                    "Friday": [],
                    "Saturday": [],
                    "Sunday": []
                }}, f)
        else:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                print(data)

    def add_task(self, task, time):
        self.tasks.append((task, time))