import mysql.connector
from mysql.connector import Error
from entity.Task_Class import Task


"""
EXEMPLE REQUETE 

INSERT INTO task 
VALUES (1, 'repassage', false);

"""

class TasksRepository:
    def __init__(self, host, database, user, password):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                port=3306,
                database=database,
                user=user,
                password=password
            )
            if self.connection.is_connected():
                print("Connexion à la base de données réussie")
            else :
                print("Connexion à la base de données échouée")
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            self.connection = None

    def create(self, task_entity) -> int:
        """
        Insère une tâche dans la base de données et retourne l'ID généré.
        :param task_entity: Instance de Task contenant les données.
        :return: ID du tâche créé.
        """
        query = """
        INSERT INTO task (id, title, is_done)
        VALUES (%s, %s, %s)
        """
       
        values = (self.connection.cursor().lastrowid, task_entity.title, task_entity.is_done)
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Erreur lors de l'ajout du tâche : {e}")
            return None

    def read_all(self):
        """
        Récupère tous les tâches sous forme d'objets Task. 
        :return: Liste d'instances de Task.
        """
        query = "SELECT * FROM task"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            tasks = cursor.fetchall() # ca donne un truc comme [{'id': 1, 'title': 'Ménage', 'is_done': 0}, {'id': 2, 'title': 'Repassage', 'is_done': 0}]
            return [Task(
                task["id"],
                task["title"],
                task["is_done"]
                ) for task in tasks]
        except Error as e:
            print(f"Erreur lors de la récupération des tâches : {e}")
            return []
    
    def read_by_id(self, task_id):
        """
        Récupère un tâche par son ID.
        :param task_id: ID tâche.
        :return: Instance de Task ou None si non trouvé.
        """
        query = "SELECT * FROM task WHERE id = %s"
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, (task_id,))
            task = cursor.fetchone()
            return Task(
                task["id"],
                task["title"],
                task["is_done"]
                ) if task else None
        except Error as e:
            print(f"Erreur lors de la récupération de la tâche : {e}")
            return None
    
    def update(self, task_entity):
        """
        Met à jour une tâche existante et retourne l'entité mise à jour.
        :param task_entity: Instance de Task contenant les nouvelles données.
        :return: Task après mise à jour, ou None en cas d'erreur.
        """
        query = """
        UPDATE task
        SET title = %s, is_done = %s
        WHERE id = %s
        """
        values = (
            task_entity.title,
            task_entity.is_done,
            task_entity.id
        )
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            if cursor.rowcount > 0:
                return self.read_by_id(task_entity.id)
            return -1
        except Error as e:
            print(f"Erreur lors de la mise à jour de la tâche : {e}")
            return None

    def delete(self, task_id):
        """
        Supprime une tâche par son ID.
        :param task_id: ID de la tâche.
        :return: Booléen indiquant si la suppression a été effectuée.
        """
        query = "DELETE FROM task WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (task_id,))
            self.connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Erreur lors de la suppression de la tâche : {e}")
            return False

    def __del__(self):
        """
        Ferme la connexion à la base de données.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connexion à la base de données fermée")
