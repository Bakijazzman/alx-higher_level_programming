-- List all shows contained in the database that have at least one genre
SELECT t.title, g.genre_id
FROM tv_shows AS t
INNER JOIN tv_show_genres AS g
ON t.shows.id = g.show_id
ORDER BY t.title, g.genre_id;
