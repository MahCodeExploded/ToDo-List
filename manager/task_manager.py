from Utilities.Validators.SQL_Validator import Validator

class List:
    """
    La liste
    """
    def __init__(self, data_base):
        self.data_base = data_base

    def add_task(self, new_task):
        """
        Demande à la database d'ajouter une tâche.
        Vérifie d'abord que la tâche entrée n'est pas vide, puis lance le détecteur d'injection SQL si celui-ci est activé via l'interface graphique.
        La vérification tâche vide est utile uniquement si la première vérification au niveau de l'interface graphique est contournée par un utilisateur malveillant
        Le détecteur d'injection SQL fonctionne mais est inutile car la couche repository fait de l'échappement de valeurs, ce qui la protège naturellement des injections SQL
        Bref, ces étapes ne sont là que pour respecter la consigne.
        NOTE : le détecteur d'injection SQL est aggressif et ne laisse rien passer. Si un utilisateur rentre une tâche "Acheter fromage", il détectera le mot-clé "FROM" et bloquera la requête.
        """
        if new_task.title.strip() : #vérifie si tâche vide
            if self.SQL_validation(new_task) :
                print("Alerte injection SQL")
                return -1
            else :
                created_task_id = self.data_base.create(new_task)
                return created_task_id
        else : 
            print ("Erreur, la tâche entrée est vide !")     

    def show_all_tasks(self) :
        task_list = self.data_base.read_all()
        return task_list

    def delete_task(self, task_id):
        self.data_base.delete(task_id)
           
    def edit_task (self, task_to_update):
        if task_to_update.title.strip() : #vérifie qu'elle n'est pas vide

            if task_to_update.id <= -2 and self.SQL_validation(task_to_update) :
                print("Alerte injection SQL")
                return -1
            elif task_to_update.id <= -2 and not self.SQL_validation(task_to_update) :
                task_to_update.id = (task_to_update.id + 2)*(-1) #redonne à l'ID sa forme originale si rien de suspect niveau SQL
                updated_task_status = self.data_base.update(task_to_update)
                return updated_task_status
            else : #envoie requete directement à la base de données si filtre SQL non activé
                updated_task_status = self.data_base.update(task_to_update)
                return updated_task_status
        else : 
            print ("Erreur, la tâche entrée est vide !")     


    def SQL_validation (self, task_to_validate) :
        SQL_detector = Validator(task_to_validate)
        return SQL_detector.anti_sql_injection_filter()


    
