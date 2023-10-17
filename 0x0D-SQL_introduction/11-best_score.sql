-- This script lists records with score >= 10 from 'second_table'
-- Execute: cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- Select records with score >= 10 from 'second_table' and order by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
