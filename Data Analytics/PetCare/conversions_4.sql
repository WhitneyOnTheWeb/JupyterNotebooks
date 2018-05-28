SELECT DATE(c.booked_at) AS booked_date
     , COUNT(DATE(c.booked_at)) AS booked_count
     , COUNT(DATE(c.cancelled_at)) AS cancelled_count
FROM conversations_conversation AS c
WHERE c.booked_at BETWEEN '2017-04-12' AND '2017-07-11' -- 90 Day Snapshot of BOOKINGS
GROUP BY DATE(c.booked_at)
ORDER BY DATE(c.booked_at) DESC
