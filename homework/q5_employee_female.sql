-- Q5. employee 테이블에서 성별이 Female인 직원의 나이와 직위(Position)을 가져오는 Query를 작성하세요(10점)
-- Query의 결과 값은 반드시 아래의 순서로 되어야 합니다.(e.g 직위가 먼저 올 경우 오답 처리됩니다.)
-- age  position
-- 25	Associate marketer
-- 45	Director

SELECT 
    age, position 
FROM 
    employee 
WHERE 
    gender = 'Female';