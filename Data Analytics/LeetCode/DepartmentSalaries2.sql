SELECT d.Name AS Department
	 , e1.Name AS Employee
	 , Salary
FROM Employee AS e1
	JOIN Department AS d 
		ON e1.DepartmentId = d.Id
        
WHERE 3 > (
	SELECT COUNT(DISTINCT e2.Salary)
	FROM Employee AS e2
	WHERE e2.Salary > e1.Salary
	AND e1.DepartmentId = e2.DepartmentId
)
ORDER BY Department, Salary DESC