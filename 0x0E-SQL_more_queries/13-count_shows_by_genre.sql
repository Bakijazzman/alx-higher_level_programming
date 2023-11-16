--displays number of shows linked to each
SELECT g.name AS genre, COUNT(t.genre_id) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_shows_genres AS t
ON g.id = t.genre_id
GROUP BY t.genre_id
ORDER BY number_of_shows DESC, g.id ASC;
