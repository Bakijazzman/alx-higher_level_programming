-- List all shows contained in the database that have at least one genre
SELECT tv.title, gen.genre_id
FROM tv_shows AS tv
INNER JOIN tv_show_genres AS gen
ON tv.shows.id = gen.show_id
ORDER BY tv.title, gen.genre_id;
