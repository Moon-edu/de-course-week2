-- Q11. visitor값이 null인 레코드를 삭제하는 쿼리를 작성하세요(10점)
-- Query의 실행 결과 데이터베이스에서 visitor가 null인 레코드가 삭제되어 검색이 되지 않아야 합니다.
-- Hint: delete를 사용하세요

--/*Q11*/
DELETE FROM VISIT_LOG
 WHERE VISITOR IS NULL;
--SELECT * FROM VISIT_LOG WHERE VISITOR IS NULL;