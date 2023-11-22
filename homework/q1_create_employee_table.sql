create table employee(
	emp_id char(6) unique not null,
	gender char(6) not null CHECK (gender IN ('Male', 'Female', 'Others')),
	name char(20) not null,
	address char(100),
	department int check (department < 100),
	manager char(6),
	age int not null check (age < 200),
	position char(30)
);


