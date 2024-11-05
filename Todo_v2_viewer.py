# views/todo_list_view_cli.py
class TodoListViewCLI:
    def display_todo_list(self, tasks):
        for idx, task in enumerate(tasks):
            status = "[x]" if task.is_done else "[ ]"
            print(f"{idx}. {status} {task.name}")

    def mark_task_as_done(self, index):
        print(f"Task {index} marked as done!")
