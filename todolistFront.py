# views/todo_list_view_pyqt6.py
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox
)
from PyQt6.QtCore import Qt

class TodoListViewPyQt6(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Todo List App')
        self.setGeometry(100, 100, 400, 300)

        # Layout principal
        self.main_layout = QVBoxLayout(self)

        # Liste des tâches
        self.list_widget = QListWidget(self)
        self.main_layout.addWidget(self.list_widget)

        # Champ d'entrée et boutons
        self.input_layout = QHBoxLayout()
        self.main_layout.addLayout(self.input_layout)

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Nouvelle tâche...")
        self.input_layout.addWidget(self.task_input)

        self.add_task_button = QPushButton("Ajouter", self)
        self.add_task_button.clicked.connect(self.add_task)
        self.input_layout.addWidget(self.add_task_button)

        self.mark_done_button = QPushButton("Marquer comme fait", self)
        self.mark_done_button.clicked.connect(self.mark_task_as_done)
        self.main_layout.addWidget(self.mark_done_button)

        self.update_list()

    def update_list(self):
        """Mise à jour de l'affichage de la liste des tâches"""
        self.list_widget.clear()
        tasks = self.controller.get_tasks()
        for idx, task in enumerate(tasks):
            status = "[x]" if task.is_done else "[ ]"
            self.list_widget.addItem(f"{idx}. {status} {task.name}")

    def add_task(self):
        """Gestion de l'ajout d'une tâche"""
        task_description = self.task_input.text().strip()
        if task_description:
            self.controller.add_task(task_description)
            self.task_input.clear()
            self.update_list()
        else:
            QMessageBox.warning(self, "Erreur", "Le champ de description de la tâche est vide !")

    def mark_task_as_done(self):
        """Marquer une tâche comme faite"""
        selected_item = self.list_widget.currentRow()
        if selected_item >= 0:
            self.controller.mark_task_as_done(selected_item)
            self.update_list()
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner une tâche à marquer comme terminée !")
