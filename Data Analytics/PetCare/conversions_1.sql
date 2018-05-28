SELECT service_type, round(AVG(price),2) avgPrice
FROM services_service
GROUP BY service_type