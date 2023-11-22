create table visit_log(
	visitor char(6),
	enter timestamp not null,
	out timestamp,
	purpose char(50)
);