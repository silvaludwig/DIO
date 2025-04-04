create schema if not exists company;

create table company.employee(
firstName varchar(15) NOT null,
middleName char,
lastName varchar(15) NOT NULL,
SSN char(9) NOT NULL,
birthdayDate DATE,
adress varchar(30),
sex char,
salary decimal(10,2),
superSSN char(9),
departmentNumber int NOT NULL,
primary key (SSN)
);

use company;
create table department(
departmentName varchar(15) NOT NULL,
departmentNumber int NOT NULL,
managerSSN char(9),
managerStartDate date,
primary key (departmentNumber),
unique (departmentNumber),
foreign key (managerSSN) references employee(SSN)
);

create table department_locations(
departmentNumber int NOT NULL,
departmentLocation varchar(15) NOT NULL,
primary key (departmentNumber, departmentLocation),
foreign key (departmentNumber) references department(departmentNumber)
);

create table project(
projectName varchar(15) NOT NULL,
projectNumber int NOT NULL,
projectLocation varchar(15),
departmentNumber int NOT NULL,
primary key (projectNumber),
unique (projectName),
foreign key (departmentNumber) references department(departmentNumber)
);

create table worksOn(
SSN char(9) NOT NULL,
projectNumber int NOT NULL,
hours decimal(3,1) NOT NULL,
primary key (SSN, projectNumber),
foreign key (SSN) references employee(SSN),
foreign key (projectNumber) references project(projectNumber)
);

create table dependent(
SSN char(9) NOT NULL,
dependentName varchar(15) NOT NULL,
dependentSex char,
birthdayDate date,
relationship varchar(8),
primary key (SSN, dependentName),
foreign key (SSN) references employee(SSN)
);

show tables;
desc worksOn;