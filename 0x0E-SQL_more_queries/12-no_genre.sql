-- List all shows contained in the database that have at least one genre
SELECT t.title, g.genre_id
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS g
ON t.id = g.show_id
WHERE g,genre_id IS NULL
ORDER BY t.title, g.genre_id;
