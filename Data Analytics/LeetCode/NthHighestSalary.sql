SELECT MAX(Salary) AS NthHighestSalary
FROM Employee AS e1
WHERE 3 = (SELECT COUNT(DISTINCT (e2.Salary)) 
           FROM Employee AS e2
           WHERE e2.Salary >= e1.Salary)