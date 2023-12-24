create table usuario(
	id SERIAL primary key,
	username varchar(20),
	body varchar(100)
);


insert into usuario (username, body) values ('emer', 'Siuuu');


select * from usuario