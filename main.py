import os
import sys
from dotenv import load_dotenv

from entity.Task_Class import Task
from repository.todo_connect_to_database import TasksRepository
from manager.task_manager import List
from controller.task_controller import TaskController
from viewer.task_interface import TodoListApp
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":

    app = QApplication(sys.argv)
    repo = TasksRepository(host="localhost", database="todotasks", user="myuser", password="mypassword")
    manager = List(repo)
    view = None 
    controller = TaskController(manager, view)
    view = TodoListApp(controller) #connecte les signaux, c'est éco+ mais as long as it works... 

    view.show()

    sys.exit(app.exec())

