-- Andrew Siluyele
-- shows and counts the number of records where score is the same
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
