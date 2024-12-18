class TaskController :

    def __init__(self, manager, view):
        self.manager = manager
        self.view = view

    def create_task (self, input_task) :
        new_task_id = self.manager.add_task(input_task)
        return new_task_id
    
    def update_task (self, modified_task) :
        task_to_modify = self.manager.edit_task(modified_task)
        return task_to_modify
    
    def read_all_tasks (self) :
        task_list = self.manager.show_all_tasks()
        return task_list
    
    def delete_task (self, input_task_id) :
        delete_status = self.manager.delete_task(input_task_id)
        return delete_status