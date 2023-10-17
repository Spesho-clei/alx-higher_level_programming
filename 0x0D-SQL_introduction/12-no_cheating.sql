-- This script updates the score of Bob to 10 in 'second_table'
-- Execute: cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- Update the score of Bob to 10
UPDATE second_table SET score = 10 WHERE name = 'Bob';
