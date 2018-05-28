SELECT friends.id AS id,
	COUNT(1) AS num
FROM
(
SELECT requester_id AS id 
FROM request_accepted
	UNION ALL 
SELECT accepter_id
FROM request_accepted
) AS friends
			 
GROUP BY id
HAVING num = (
	SELECT MAX(num) AS max
	FROM
	(
	SELECT friends.id AS id, COUNT(1) AS num
		FROM
		(
		SELECT requester_id AS id 
		FROM request_accepted
			UNION ALL 
		SELECT accepter_id
		FROM request_accepted
		) AS friends
        
	GROUP BY id
	) AS max
)
ORDER BY id DESC
