-- 이 파일을 제대로 작성하지 않거나, 오답일 경우 자동으로 Q4, Q7, Q8, Q9, Q12이 오답 처리됩니다.
-- Q3. visit_log 테이블을 생성하시오. 테이블의 스펙은 아래와 같습니다.
-- 1. visitor는 null값이 허용되며, null일 경우 직원이 아닌 외부 손님으로 간주됩니다. 직원일 경우 직원의 ID가 기록됩니다
-- 2. enter, out 는 출입 시간을 기록하는 데이터로 enter는 null이 될 수 없고, out은 null이 될 수 있습니다.
-- 3. purpose는 최대 50자까지 허용되며, null값이 허용됩니다.

--/*Q3*/
CREATE TABLE VISIT_LOG (
	   VISITOR VARCHAR(6)
	 , ENTER   TIMESTAMP  NOT NULL
	 , OUT     TIMESTAMP
	 , PURPOSE VARCHAR(50) )
	 ;