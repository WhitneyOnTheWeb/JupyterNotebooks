SELECT d.Name AS Department
	 , e.Name AS Employee
	 , Salary
FROM Employee AS e
	JOIN Department AS d 
		ON e.DepartmentId = d.Id
        
WHERE (e.DepartmentId, Salary) IN (
	SELECT DepartmentId, MAX(Salary)
	FROM Employee AS e
	GROUP BY DepartmentId
)
ORDER BY Salary DESC