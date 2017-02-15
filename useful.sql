SELECT
      id
    , score
    , @curr_rank := IF(@prev_rank = score, @curr_rank, @curr_rank + 1) AS rank
    , @prev_rank := score
  FROM practices.Scores, (SELECT @curr_rank := 0) r,(SELECT @prev_rank := NULL) p
  ORDER BY score DESC;



select department,employee, salary
from salaries b
where (SELECT count(distinct salary) from salaries a WHERE a.salary >= b.salary and a.department = b.department ) in (1,2);



select a.department,a.employee, a.salary, count(distinct b.salary) FROM salaries a JOIN salaries b 
on a.salary <= b.salary 
and a.department = b.department
GROUP BY a.department,a.employee,a.salary;