

# NOTE : METTRE DES SETTERS 
class Task :
    def __init__(self, name):
        self.name = name
        self.isdone = False

class TodoList :
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task:str) :
        if task.strip() : #si la chaine n'est PAS vide une fois que tous les espaces ont été retirés
            self.tasks.append(Task(task))
            return self.tasks[- 1] #ca va retourner un objet, aka la dernière tache ajoutée
        else :
            return False #chaine ne contient que des espaces
        
    def task_done (self, index) :
        if self.tasks and 0 <= index < len(self.tasks) :
            self.tasks[index].isdone = True
            return self.tasks[index].isdone #renvoie True
        else :
            print("mauvais index")
            return False
    
    def get_tasks(self):
        return self.tasks #retourne une liste, celle des tâches

class ToDoListManager :
    def __init__(self, todo_list, persistence): # ? pour le persistence ?
        self.todo_list = todo_list #un objet todo list
        self.persistence = persistence #objet CSVPersistence ?

    def add_task (self, description) :
        self.todo_list.add_task(description)

    def delete_task(self, task):
        None
    
    def mark_task_as_done(self,index) :
        if self.todo_list.tasks and 0 <= index < len(self.todo_list.tasks) :
            return self.todo_list.task_done(index)
        else :
            print("wrong index")
            return False    
    def get_tasks (self):
        return self.todo_list.get_tasks()
    def save(self) : #persistence
        return self.persistence.save(self.todo_list)

    def load(self) :
        return self.persistence.load()

    def notify_observers(self) :
        None

from abc import ABC, abstractmethod
import csv
class Persistance(ABC):
    @abstractmethod
    def save(self, todo_list):
        pass
    @abstractmethod
    def load(self):
        pass

class CSVPersistance:
    def __init__(self):
        None

    def save(self,todo_list):#sauvegarde la liste sur le fichier
        None 

    def load(self):#charge le fichier
        None 



class CsvPersistence(Persistance):
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, todo_list):
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for task in todo_list.get_tasks():
                writer.writerow([task.name, task.isdone])

    def load(self):
        todo_list = TodoList()
        try:
            with open(self.file_name, newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    task = Task(row[0])
                    if row[1] == 'True':
                        task.isdone = True
                    todo_list.add_task(task)
        except FileNotFoundError:
            pass
        return todo_list