SELECT num.friends AS id,
		 COUNT(1) AS num
	FROM
	(
	 SELECT requester_id AS friends 
	 FROM request_accepted
		UNION ALL 
	 SELECT accepter_id
	 FROM request_accepted
	) AS num
	 
GROUP BY num.friends
ORDER BY num DESC
LIMIT 1