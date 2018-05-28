SELECT ts.test_group AS test_group,
       COUNT(c.id) conv_total,
       COUNT(c.booked_at) booked_total
FROM services_service AS s
    JOIN conversations_conversation AS c ON s.id = c.service_id
        JOIN people_testsegmentation AS ts ON ts.id = c.requester_id
GROUP BY ts.test_group