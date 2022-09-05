-- In order to make sure I was writing valid SQL.
-- I used this queries against mariadb. 

CREATE TABLE admins (
	id INT,
	username VARCHAR(10),
	`password` VARCHAR(10)
);

INSERT INTO admins (id, username, password) values (99, 'admin', 'admin');


SELECT password FROM admins WHERE username=''INSERT INTO admins (id, username, password) values (99, 'admin', 'admin');--'