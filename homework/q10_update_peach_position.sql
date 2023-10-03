-- Q10. Peach의 position을 Senior engineer로 수정하는 쿼리를 작성하세요(10점)
-- Query의 실행 결과 데이터베이스에서 Peach의 직위가 Senior engineer로 수정되어 있어야 합니다.


--/*Q10*/
UPDATE EMPLOYEE SET POSITION = 'SENIOR ENGINEER'
 WHERE NAME = 'PEACH';
--SELECT * FROM EMPLOYEE WHERE NAME = 'PEACH';