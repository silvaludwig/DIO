SHOW databases;

create database if not exists first_example;
use first_example;

CREATE TABLE person(
	person_id smallint unsigned,
	firstName varchar(20),
	lastName varchar(20),
	gender ENUM('M', 'F'),
	birthDate date, 
	street varchar(30),
	city varchar(20),
	state varchar(20),
	country varchar(20), 
	postalCode varchar(20),
    constraint pk_person primary key (person_id)
);

desc person;

create table favorite_food(
	person_id smallint unsigned,
    food varchar(20),
    constraint pk_favorite_food primary key (person_id, food),
    constraint pf_favorite_food_person_id foreign key (person_id) 
    references person(person_id)
);

desc favorite_food;

show databases;

INSERT INTO person VALUES ('2', 'Carolina', 'Silva', 'F', '1979-05-26', 'Rua Exemplo', 'Cidade exemplo', 'MG', 'Brasil', '12345-678');

SELECT * FROM person;

INSERT INTO person VALUES	('1', 'Joana', 'Silva', 'F', '1979-05-26', 'Rua Exemplo', 'Cidade exemplo', 'MG', 'Brasil', '12345-678'),
							('2', 'Francisca', 'Silva', 'F', '1979-05-26', 'Rua Exemplo', 'Cidade exemplo', 'MG', 'Brasil', '12345-678'),
                            ('3', 'João', 'Silva', 'M', '1979-05-26', 'Rua Exemplo', 'Cidade exemplo', 'MG', 'Brasil', '12345-678');
                        
DELETE FROM person WHERE person_id=2 or person_id=4 or person_id=5;

desc favorite_food;

INSERT INTO favorite_food VALUES 	(1, 'lasanha'),
									(2, 'Carne Assada'),
                                    (3, 'Pizza');

SELECT * FROM favorite_food;

DELETE FROM favorite_food WHERE person_id=1;


