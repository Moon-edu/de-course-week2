-- Q8. 방문 목적별 총 방문 횟수를 가져오는 쿼리를 작성하세요(10점)
-- Query의 결과 값은 어떤 순서로 되더라도 상관 없습니다.
-- 결과 값은 아래와 같이 방문목적, 총 방문 횟수 순으로 되어야 합니다.
-- purpose	    count
-- meeting	    2
-- interview	1

select purpose, count(purpose) from visit_log group by purpose;