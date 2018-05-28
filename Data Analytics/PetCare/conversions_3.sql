SELECT r.stars AS rating,
       COUNT(reviewer_id), 
       CASE WHEN reviewer_id < (SELECT MAX(provider_id)
                                FROM services_service AS s) 
       THEN 'provider' ELSE 'owner' END AS person
FROM conversations_review AS r
    JOIN people_person AS p ON p.id = r.reviewer_id
        JOIN conversations_conversation AS c ON c.id = r.conversation_id
WHERE c.booked_at IS NOT NULL 
    AND c.cancelled_at IS NULL -- Service booked and not cancelled
GROUP BY person, r.stars