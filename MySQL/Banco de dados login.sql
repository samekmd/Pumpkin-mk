create database login;
use login;
create table login
(
    nome varchar(60), 
    senha varchar(60)
);

SELECT * FROM login;

INSERT INTO login (nome,senha)
VALUES ('samuel', 'Flask-DB', 'HTML, CSS, MySQL');