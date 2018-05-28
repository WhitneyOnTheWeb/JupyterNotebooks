SELECT ts.test_group AS test_group,
       COUNT(c.id) conv_total,
       COUNT(c.booked_at) booked_total
FROM conversations_conversation AS c
        JOIN people_testsegmentation AS ts ON ts.id = c.requester_id
WHERE DATE(c.added) > '2017-03-13'
GROUP BY ts.test_group