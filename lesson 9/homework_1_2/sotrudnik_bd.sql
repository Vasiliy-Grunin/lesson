CREATE DATABASE IF NOT EXISTS sotrudnik;
USE sotrudnik;
CREATE TABLE IF NOT EXISTS sotrudnik(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
	first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    position_in_company VARCHAR(30) NOT NULL,	
    money INT NOT NULL
    );
INSERT INTO sotrudnik(id, first_name, last_name, position_in_company, money) VALUES ( null,'Albert' ,'Tvoy','manager',25000);
INSERT INTO sotrudnik(id, first_name, last_name, position_in_company, money) VALUES ( null,'Ivan', 'Grunin','developer',10000);

