class List:
    """
    La liste
    """
    def __init__(self, data_base):
        self.data_base = data_base

    def add_task(self, new_task):
        if new_task.title.strip() : 
            #vérifie que la tâche entrée n'est pas vide.
            #utile uniquement si la première vérification au niveau de l'interface graphique est contournée par un utilisateur malveillant
            #(ce qui ne se produira pas dans notre cas d'utilisation)
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
        self.data_base.update(task_to_update)
