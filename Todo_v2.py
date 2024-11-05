# models/task.py
class Task:
    def __init__(self, name):
        self.name = name
        self.is_done = False

    def mark_as_done(self):
        self.is_done = True

# models/todo_list.py
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_done()

    def get_tasks(self):
        return self.tasks

# persistence/persistence.py
import abc

class Persistence(abc.ABC):
    @abc.abstractmethod
    def save(self, todo_list):
        pass

    @abc.abstractmethod
    def load(self):
        pass

# persistence/csv_persistence.py
import csv

class CsvPersistence(Persistence):
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, todo_list):
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for task in todo_list.get_tasks():
                writer.writerow([task.name, task.is_done])

    def load(self):
        todo_list = TodoList()
        try:
            with open(self.file_name, newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    task = Task(row[0])
                    if row[1] == 'True':
                        task.mark_as_done()
                    todo_list.add_task(task)
        except FileNotFoundError:
            pass
        return todo_list
