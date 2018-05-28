SELECT c.id AS conv,
       DATE(c.added) AS conv_date,
       CASE WHEN c.booked_at IS NULL 
            THEN '0' 
            ELSE '1' END AS is_booked,
       ts.test_group
FROM conversations_conversation AS c 
        JOIN people_testsegmentation AS ts ON ts.id = c.requester_id
WHERE DATE(c.added) > '2017-03-13'