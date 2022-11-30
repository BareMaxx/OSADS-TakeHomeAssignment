CREATE DATABASE personsdatabase;

use personsdatabase;

CREATE TABLE person (
	PersonID int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	Firstname varchar(255) NOT NULL,
	Lastname varchar(255) NOT NULL
);

INSERT INTO person (Firstname, Lastname) VALUES ("Mads", "Jensen");
INSERT INTO person (Firstname, Lastname) VALUES ("Mathias", "Neerup");