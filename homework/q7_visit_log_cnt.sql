-- Q7. 2022년 7월 12일 총 방문 횟수를 가져오는 쿼리를 작성하세요(10점)
-- Query의 결과 값은 반드시 총 방문 횟수(정수형 숫자)이어야합니다.
-- Hint: 집계 함수 count를 사용하세요
select count(*) as visit_cnt
from visit_log
where 1=1
and enter >= '2022-07-12 0:00:00'
and enter < '2022-07-13 0:00:00'
;