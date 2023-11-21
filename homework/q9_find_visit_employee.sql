-- Q9. 2022-07-11 09:00:00 에 방문한 사람의 이름과 부서 번호, 사번(emp_id)을 가져오는 쿼리를 작성하세요(10점)
-- Query의 결과 값은 아래와 같이 이름, 부서 번호, 사번 순으로 되어야 합니다.
-- name	department	emp_id
-- John	1	        A00001
-- 쿼리의 결과 순서는 상관 없습니다.
-- Hint: join을 사용하세요

select e.name
     , e.department
     , e.emp_id
from employee e
     join visit_log v on e.emp_id = v.visitor
where 1=1
and enter = '2022-07-11 09:00:00'
;