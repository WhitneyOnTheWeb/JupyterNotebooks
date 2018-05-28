SELECT COUNT(reviewer_id) AS total_reviews
FROM conversations_review AS r
    JOIN conversations_conversation AS c ON c.id = r.conversation_id
WHERE c.booked_at IS NOT NULL 
    AND c.cancelled_at IS NULL -- Service booked and not cancelled