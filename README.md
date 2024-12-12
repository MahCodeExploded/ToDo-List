# ToDo-List
ToDoList

Pour faire marcher ce projet, créer une database MySQL via le sql suivant :



CREATE DATABASE todotasks;

USE todotasks ;

CREATE TABLE task (
id INT AUTO_INCREMENT PRIMARY KEY,
 title VARCHAR(255) NOT NULL, 
 is_done BOOLEAN DEFAULT FALSE
);


CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';


GRANT SELECT, INSERT, UPDATE, DELETE ON todotasks.* TO 'myuser'@'localhost';
