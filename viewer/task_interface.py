from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, 
    QCheckBox, QWidget, QSpacerItem, QSizePolicy, QMessageBox, QInputDialog
)
from PyQt6.QtCore import Qt
from entity.Task_Class import Task

class TodoListApp(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 600)
        self.controller = controller

        # Main Widget et Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # input field + bouton pour nouvelles tâches
        self.input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Entrez une tâche...")
        self.add_task_button = QPushButton("Ajouter tâche")
        self.add_task_button.clicked.connect(self.add_task)
        self.input_layout.addWidget(self.task_input)
        self.input_layout.addWidget(self.add_task_button)
        self.layout.addLayout(self.input_layout)

        # Placeholder pour tâches
        self.tasks_layout = QVBoxLayout()
        self.layout.addLayout(self.tasks_layout)

        # alignement depuis le haut
        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        
        #cherche les tâches existantes dans la base pour les afficher :
        if self.controller : #une fois que le controller est ajouté, balancer la liste des tâches
            self.display_tasks()

    # récupérer la liste des tâche existantes dans la database :
    def display_tasks(self):
        task_list = self.controller.read_all_tasks()
        if task_list :
            for task in task_list:
                self._create_task_widget(task.title, task.id)

    #ajouter une nouvelle tâche 
    def add_task(self):
        task_text = self.task_input.text().strip()

        if not task_text: #première sécurité contre une entrée vide (une seconde se trouve dans la BLL au cas où)
            QMessageBox.warning(self, "Attention", "Le texte de la tâche ne peut pas être vide.")
            return
        
        self.task_input.clear()
        new_task_ID = self.controller.create_task(Task(-1, task_text, False)) #envoie la nouvelle tâche crée à la couche suivante du programme sous forme d'un objet Task, récupère son ID dans la database en retour
        self._create_task_widget(task_text, new_task_ID)

    #Afficher une tâche dans la liste
    def _create_task_widget(self, task_text, task_id):
        task_widget = QWidget()
        task_layout = QHBoxLayout(task_widget)
        task_layout.setContentsMargins(0, 0, 0, 0)

        # Checkbox, si cochée tâche barrée
        checkbox = QCheckBox()
        checkbox.setObjectName(f"check_{task_id}") #le nom de la checkbox comprend l'ID database de la tâche associée afin de pouvoir le réutiliser.
        checkbox.setText(task_text)
        checkbox.stateChanged.connect(lambda state: self._toggle_task_strike(checkbox))
        task_layout.addWidget(checkbox)

        # Bouton modifier 
        edit_button = QPushButton("M")
        edit_button.setFixedSize(30, 30)  # Bouton carré
        edit_button.setObjectName(f"edit_{task_id}") #le nom du bouton comprend l'ID database de la tâche associée afin de pouvoir le réutiliser.
        edit_button.clicked.connect(lambda: self._edit_task(checkbox))
        task_layout.addWidget(edit_button)

        # Bouton supprimer
        delete_button = QPushButton("X")
        delete_button.setFixedSize(30, 30)  # Bouton carré
        delete_button.setObjectName(f"del_{task_id}") #le nom du bouton comprend l'ID database de la tâche associée afin de pouvoir le réutiliser
        delete_button.clicked.connect(lambda: self._delete_task(task_widget))
        task_layout.addWidget(delete_button)

        self.tasks_layout.addWidget(task_widget)
    
    #cochage des checkbox = texte barré, tâche marquée comme effectuée dans la database
    def _toggle_task_strike(self, checkbox):
        font = checkbox.font()
        font.setStrikeOut(checkbox.isChecked()) #accorde la police de la tâche (barrée ou non) au statut (cochée ou non) de sa box
        checkbox.setFont(font)

        sender = self.sender()  # Récupère la checkbox qui a émis le signal
        checkbox_id = sender.objectName() #choppe son nom
        task_id = int(checkbox_id.replace("check_", "")) #extrait l'ID du str de son nom
        self.controller.update_task(Task(task_id, checkbox.text(), (checkbox.isChecked()))) #accorde le statut is_done de la tâche correspondante au statut coché ou non de sa checkbox

    def _edit_task(self, checkbox):
        sender = self.sender()  # Récupère le bouton qui a émis le signal
        button_id = sender.objectName() #choppe son nom
        task_id = int(button_id.replace("edit_", "")) #extrait l'ID du str de son nom

        new_text, ok = QInputDialog.getText(self, "Modifier tâche", "Entrez le nouveau texte de la tâche :", text=checkbox.text())
        if ok and new_text.strip():
            checkbox.setText(new_text.strip())
            print(new_text.strip())
            self.controller.update_task(Task(task_id, new_text.strip(), False))

    def _delete_task(self, task_widget):
        sender = self.sender()  # Récupère le bouton qui a émis le signal
        button_id = sender.objectName() #choppe son nom
        task_id = int(button_id.replace("del_", "")) #extrait l'ID du str de son nom

        self.controller.delete_task(task_id) #transmet l'ID au controller

        self.tasks_layout.removeWidget(task_widget)
        task_widget.deleteLater()

    
