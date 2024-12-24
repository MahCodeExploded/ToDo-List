Pour faire marcher ce projet, créer une database MySQL via le sql suivant :

- - - - - 

CREATE DATABASE todotasks;

USE todotasks ;

CREATE TABLE task (
id INT AUTO_INCREMENT PRIMARY KEY,
 title VARCHAR(255) NOT NULL, 
 is_done BOOLEAN DEFAULT FALSE
);


CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';


GRANT SELECT, INSERT, UPDATE, DELETE ON todotasks.* TO 'myuser'@'localhost';

- - - - - 

AUTRES NOTES :

- Le validateur SQL n'est là que pour la consigne. Le texte entré par l'utilisateur est considéré comme du texte simple et ne peut pas être utilisé comme injection SQL (c'est protégé au niveau du Repository, code échappé).
- Le validateur est agressif.
- Pour ces deux raison, le validateur est désactivable via une checkbox. Ce ne serait pas le cas dans un produit à destination de l'utilisateur, mais c'est juste à destination du professeur corrigeant ce projet.
- Le module de tests unitaires du validateur SQL peut être lancé indépendamment, il se trouve dans le même dossier que le validateur (Utilities/validator)
