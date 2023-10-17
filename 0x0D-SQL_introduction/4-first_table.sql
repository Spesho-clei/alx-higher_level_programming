-- This script creates the table 'first_table' if it doesn't already exist
-- Exceute: cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
