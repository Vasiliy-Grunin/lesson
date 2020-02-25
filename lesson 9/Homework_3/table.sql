create database if not exists company;
use company;
create table if not exists chef(
	id int unsigned not null auto_increment primary key,
    first_name varchar(30) not null,
    last_name varchar(30) not null,
    position_in_company varchar(30) not null,
    worker int not null
)engine=InnoDB;

create table if not exists worker(
	id int unsigned not null auto_increment primary key,
    first_name varchar(30) not null,
    last_name varchar(30) not null,
    position_in_company varchar(30) not null,
    chef int not null
)engine=InnoDB;

create table if not exists comminucate(
	chef INT NOT NULL,
    worker INT NOT NULL,
    primary key (chef, worker)
)engine=InnoDB;      

insert into chef (id, first_name, last_name, position_in_company, worker) values (null,'Masha', 'Griboedova','manager', 2);
insert into chef (id, first_name, last_name, position_in_company, worker) values (null,'Grisha', 'Gorbunov','manager', 1);
insert into worker (id, first_name, last_name, position_in_company, chef) values (null,'Masha', 'Griboedova','manager', 2);
insert into worker (id, first_name, last_name, position_in_company, chef) values (null,'Petay', 'Ivanov','developer', 1);
insert into worker (id, first_name, last_name, position_in_company, chef) values (null,'Ivan', 'Ivanov','developer', 2);


        
        
        
        
        
        
        
        
        