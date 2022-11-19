create table visit_log(
	visitor varchar(6) null,
	enter timestamp not null,
	out timestamp,
	purpose varchar(50)
)