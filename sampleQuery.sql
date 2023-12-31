-- Incorrect capitalization and inconsistent indentation
select employeeID, FirstName, lastName
from employee
where Salary > 50000;

-- Misspelled column name and inconsistent aliasing
select EmployeeID, First_Name as last_name, hireDate
from employee
where Salary < 70000;

-- Use of wildcard without specifying columns
select *
from employee
where HireDate > '2022-01-01';

-- Incorrect use of reserved words as identifiers
select *
from select
where from = '2022-01-01';

-- Poorly formatted update statement
update Employee set Salary = Salary * 1.1 where EmployeeID = 1;

-- Incorrect spacing in delete statement
delete from Employeewhere EmployeeID = 2;

-- Incorrect usage of transaction
begin transaction
update Employee set Salary = Salary * 1.05 where EmployeeID = 3;
commit;
