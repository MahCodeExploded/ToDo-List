# controllers/todo_list_controller.py
from Todo_v2 import TodoList
class TodoListController:
    def __init__(self, manager, view):
        self.manager = manager
        self.view = view

    def add_task(self, description):
        self.manager.add_task(description)
        self.refresh_view()

    def mark_task_as_done(self, index):
        self.manager.mark_task_as_done(index)
        self.refresh_view()

    def save(self):
        self.manager.save()

    def load(self):
        self.manager.load()
        self.refresh_view()

    def refresh_view(self):
        tasks = self.manager.get_tasks()
        self.view.display_todo_list(tasks)

# managers/todo_list_manager.py
class TodoListManager:
    def __init__(self, persistence):
        self.todo_list = TodoList()
        self.persistence = persistence

    def add_task(self, description):
        task = Task(description)
        self.todo_list.add_task(task)

    def mark_task_as_done(self, index):
        self.todo_list.mark_task_as_done(index)

    def get_tasks(self):
        return self.todo_list.get_tasks()

    def save(self):
        self.persistence.save(self.todo_list)

    def load(self):
        self.todo_list = self.persistence.load()
