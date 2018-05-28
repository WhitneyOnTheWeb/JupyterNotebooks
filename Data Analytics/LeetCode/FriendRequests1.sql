SELECT 
ROUND(
  IFNULL(
    (
    (SELECT 1.0 * COUNT(*)
     FROM (SELECT DISTINCT requester_id, accepter_id
           FROM request_accepted) AS a) -- Accepted
     
    /  -- COUNT(Accpted) / COUNT(Sent)
    
    (SELECT COUNT(*)
     FROM (SELECT DISTINCT sender_id, send_to_id
           FROM friend_request) AS s) -- Sent
    ), 
  0), 
2) AS accept_rate