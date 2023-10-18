-- Use COUNT and GROUP BY clause
-- Execute: cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT tv_show_genres.genre_id AS genre,
       COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
