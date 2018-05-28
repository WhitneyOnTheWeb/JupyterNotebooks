SELECT a.month AS month
	, IF(r.requested = 0, 0.00, 
	  ROUND(a.accepted / r.requested, 2)) AS accept_rate
FROM
	(SELECT 1.0 * COUNT(DISTINCT requester_id, accepter_id) AS accepted,
	 MONTH(accept_date) AS month 
	 FROM request_accepted) AS a
   ,
	(SELECT COUNT(DISTINCT sender_id, send_to_id) AS requested,
	 MONTH(request_date) AS month 
	 FROM friend_request) AS r

WHERE a.month = r.month
GROUP BY a.month
