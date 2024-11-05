# main.py
import sys
from PyQt6.QtWidgets import QApplication
from controllers.todo_list_controller import TodoListController
from managers.todo_list_manager import TodoListManager
from persistence.csv_persistence import CsvPersistence
from views.todo_list_view_pyqt6 import TodoListViewPyQt6

def main():
    app = QApplication(sys.argv)

    # Setup Persistence, Manager, and Controller
    persistence = CsvPersistence('tasks.csv')
    manager = TodoListManager(persistence)
    controller = TodoListController(manager, None)  # Pas encore de vue attachée

    # Setup View
    view = TodoListViewPyQt6(controller)
    controller.view = view  # Attacher la vue au contrôleur

    # Charger les tâches et afficher l'interface
    controller.load()
    view.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
