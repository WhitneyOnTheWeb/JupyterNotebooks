SELECT DATE(date_joined) AS date_joined
     , COUNT(p.id) AS users_joined
FROM people_person AS p
WHERE p.channel = 'Google'
GROUP BY DATE(date_joined)
ORDER BY date_joined