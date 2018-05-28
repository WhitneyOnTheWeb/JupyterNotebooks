SELECT service_type, COUNT(booked_at) booked_count
FROM services_service AS s
    INNER JOIN conversations_conversation AS c ON s.id = c.service_id
GROUP BY service_type;