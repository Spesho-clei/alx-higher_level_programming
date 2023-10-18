-- Create a table and database
-- Execute: cat 6-states.sql | mysql -hlocalhost -uroot -p 
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `states`
(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	name VARCHAR(256)
);
