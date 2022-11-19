create table employee(
	emp_id text unique not null,
	gender varchar(10) not null,
	name varchar(20) not null,
	address varchar(100) null,
	department smallint null,
	manager char(100) null,
	age int not null,
	position text null
)