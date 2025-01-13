from datetime import datetime

class Task:
    def __init__(self, due_date=None, priority=5, title="Choose a Title", category="Choose a Category", status="What is the status of this task?"):
        self.priority = priority
        self.title = title
        self.category = category
        self.status = status
        self.due_date = due_date
        self.creation_time = datetime.now()

    def update_priority(self, priority):
        self.priority = priority
    
    def update_title(self, title):
        self.title = title

    def update_category(self, category):
        self.category = category
    
    def update_status(self, status):
        self.status = status

    def update_due_date(self, due_date):
        self.due_date = due_date

    def print_task(self):
        print(self.title)
        print(self.priority)
        print(self.category)
        print(self.status)


    