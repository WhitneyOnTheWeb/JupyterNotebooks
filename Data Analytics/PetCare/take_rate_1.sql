SELECT s.id AS service_id
    , CAST(STRFTIME('%Y%m%d', DATE(booked_at)) AS INT) AS booked_at
    , STRFTIME('%d', DATE(booked_at)) AS day
    , STRFTIME('%m', DATE(booked_at)) AS month
    , STRFTIME('%Y', DATE(booked_at)) AS year
    , booking_total
    , (booking_total * p.fee) AS owner_fee
    , (booking_total + p.fee) AS gross_billings
    , (booking_total * s.fee) AS service_fee
    , (booking_total * p.fee) + (booking_total * s.fee) AS net_revenue
    , (booking_total + p.fee) - (p.fee + s.fee) AS provider_payment
FROM conversations_conversation AS c
    JOIN services_service AS s ON s.id = c.service_id
        JOIN people_person AS p on p.id = c.requester_id
WHERE booked_at IS NOT NULL
ORDER BY booked_at