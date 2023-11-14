-- selection of similar
SELECT score, COUNT(score) as number FROM second_table GROUP score ORDER BY number DESC;
