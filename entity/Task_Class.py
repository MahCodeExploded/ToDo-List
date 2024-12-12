class Task :
    """
    Une tâche est définie par son ID, son nom et son statut de complétion.
    """
    def __init__(self, id=None, title=None, is_done=None):
        self.id = id
        self.title = title
        self.is_done = is_done

    def __str__(self):
        return f"TaskEntity(id={self.id}, title={self.title}, is_done={self.is_done}) "
    
