-- 아래의 데이터를 넣는 쿼리를 작성해주세요.
-- 첫 줄은 테이블의 컬럼명입니다.
-- 두 번째 줄부터는 테이블의 데이터입니다.
-- 테이블의 컬럼명과 데이터는 탭으로 구분되어 있습니다.


-- emp_id	gender	name	address	                    department	manager	age	position
-- A00001	Male	Moon	10-199, Gang-nam, Seoul	    1	        C00001	30	Senior engineer
-- B00100	Female	Sun	    587/8, Gwan-ak, Seoul	    2	        B00102	25	Associate marketer
-- A08771	Others	Peach	203-3, Guro, Seoul	        1	        C00001	26	Junior engineer
-- C00129	Male	Alex	20-331, Bundang, Gyonggi	3	        C00002	40	Director
-- C00001	Male	Lion	53-3, Namyang-ju, Gyonghi	1	        C00000	55	CTO
-- C00002	Others	Cindy	100, Jong-ro, Seoul	        3	        C00000	52	Director
-- B00102	Female	Ran	    290-10, Gwanghwamun, Seoul	2	        C00000	45	Director
-- C00000	Male	K	    1010, Sung-soo, Seoul		                    51	CEO

-- K의 department와 manager의 값은 빈 문자열('')이 아닌 null입니다, 빈 문자열을 넣을 경우 오답처리됩니다.

--/*Q2*/
INSERT INTO EMPLOYEE (EMP_ID, GENDER, NAME, ADDRESS, DEPARTMENT, MANAGER, AGE, POSITION)
VALUES
  ('A00001', 'MALE'  , 'MOON' ,'10-199, GANG-NAM, SEOUL'    , 1, 'C00001', 30 , 'SENIOR ENGINEER')
 ,('B00100', 'FEMALE', 'SUN'  ,'587/8, GWAN-AK, SEOUL'      , 2, 'B00102', 25 , 'ASSOCIATE MARKETER')
 ,('A08771', 'OTHERS', 'PEACH','203-3, GURO, SEOUL'         , 1, 'C00001', 26 , 'JUNIOR ENGINEER')
 ,('C00129', 'MALE'  , 'ALEX' ,'20-331, BUNDANG, GYONGGI'   , 3, 'C00002', 40 , 'DIRECTOR' )
 ,('C00001', 'MALE'  , 'LION' ,'53-3, NAMYANG-JU, GYONGHI'  , 1, 'C00000', 55 , 'CTO')
 ,('C00002', 'OTHERS', 'CINDY','100, JONG-RO, SEOUL'        , 3, 'C00000', 52 , 'DIRECTOR')
 ,('B00102', 'FEMALE', 'RAN'  ,'290-10, GWANGHWAMUN, SEOUL' , 2, 'C00000', 45 , 'DIRECTOR')
 ,('C00000', 'MALE'  , 'K'    ,'1010, SUNG-SOO, SEOUL'      ,NULL, NULL  , 51 , 'CEO')
 ;
