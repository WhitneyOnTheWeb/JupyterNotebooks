SELECT Name AS Customers
FROM Customers AS c1
WHERE c1.Id NOT IN (SELECT c2.Id
                    FROM Customers AS c2
                        JOIN Orders AS o 
                            ON o.CustomerId = c2.Id)
