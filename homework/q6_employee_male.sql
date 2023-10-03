-- Q6. employee 테이블에서 남성의 이름, 나이, 직위를 가져오되 나이가 많은 순으로 정렬해서 가져오는 쿼리를 작성하세요(10점)
-- Query의 결과 값은 반드시 아래의 순서로 되어야 합니다.(e.g 직위가 먼저 올 경우 오답 처리됩니다.)
-- name	    age	    position
-- Lion	    55	    CTO
-- K        51      CET
-- Alex	    40	    Director
-- Moon	    30	    Senior engineer


--/*Q6*/
 select name, age, position
   from employee
  where gender= 'Male'
  order by age desc;

