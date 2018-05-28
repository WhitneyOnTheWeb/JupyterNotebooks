SELECT date_table.dates AS date,
       IFNULL(ROUND(
	COUNT(DISTINCT requester_id, accepter_id) / 
	COUNT(DISTINCT sender_id, send_to_id)
     , 2), 0.00) AS accept_rate
     
FROM request_accepted AS a, friend_request AS r,
(
  SELECT request_date AS dates 
  FROM friend_request
	UNION
  SELECT accept_date 
  FROM request_accepted
	ORDER BY dates
) AS date_table

WHERE a.accept_date <= date_table.dates
AND r.request_date <= date_table.dates
GROUP BY date_table.dates