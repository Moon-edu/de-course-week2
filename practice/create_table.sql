
--Table 생성
CREATE TABLE student(
	name varchar(10) NOT null, --이름은 최대 10자까지 문자
	phone char(11) UNIQUE NOT null, --전화번호는 최대 11자까지 문자열, 중복될 수 없음
	age int NOT null,--나이는 정수
	class varchar(50) NOT null --수업명은 최대 50자 문자열 
);



CREATE TABLE class(
	title varchar(50) not null,
	teacher varchar(10) not null,
	max_student int not null
);

--Table 삭제 
truncate student;

trunncat class;

select count(*) from perf_test

select * from student s 


create table users(user_id varchar(100), pw varchar(100));

create table perf_test(a int, b varchar(100), c varchar(100), d varchar(100));

drop table perf_test

insert into users values('a', '12345');
insert into users values('b', '12345');
insert into users values('c', '12345');

truncate users

select * from users
 

--레코드 생성
INSERT INTO student(name, phone, age, class) values('김학생', '01012345678', 20, '수학1');

INSERT INTO student values('현공부', '01033201238', 21, '영어2');

--학생 이름이 오선생, 전화번호가 01029083072, 나이가 27, 수강과목이 수학2인 학생을 새로 추가할 것

insert into student()

INSERT INTO student(name, phone, age, class) values('오선생', '01029083072', 27, '수학2');


--과목명이 물리1, 강사명이 박물리, 수강 정원이 3명인 과목을 새로 추가할 것

insert into class(title, teacher, max_student) values('물리1', '박물리', 3)
insert into class values('물리1', '박물리', 3);

insert into class(title, teacher, max_student) values('수학1', '박수학', 20)

insert into class(title, teacher, max_student) values('영어2', '홍영어', 100)


--모든 데이터 가져오기
select * from class;

select teacher from class;

select * from student;

--조건에 만족하는 데이터 가져오기
select * from student where class='수학1';

select * from student where age < 25 or class='수학1';


--수강 과목이 영어2의 최대 정원이 몇 명인지 검색해볼 것
select max_student from class where title='영어2'

--정렬하기
INSERT INTO student(name, phone, age, class) values('구영호', '01029091234', 27, '체육1');
INSERT INTO student(name, phone, age, class) values('서강일', '01029765432', 21, '국어1');


select * from student  order by age

select * from student order by age desc

select * from student order by age asc, name asc



--모든 데이터 수정하기
update class set max_student=100;

update student set phone='01098765432' where name='김학생'

update student set phone='01098765432' where name='현공부' --x

--수학 1 담당 선생을 홍길동으로 바꿔보기
update class set teacher='홍길동' where title='수학1'

update student set age=age+1


--학생 테이블 전체 삭제
delete from student

--수업 테이블 전체 삭제
delete from class

--더 빠르게 전체 삭제
truncate student

truncate class

--특정 조건을 만족하는 레코드 삭제1
delete from class where title='영어2'


-- 수업 테이블과 학생 테이블 조인
truncate class;

insert into class values('체육1', '안튼튼', 30);
insert into class values('국어1', '나랏말', 5);
insert into class values('수학2', '윤산수', 20);
insert into class(title, teacher, max_student) values('물리1', '박물리', 3);
insert into class(title, teacher, max_student) values('수학1', '박수학', 20);
insert into class(title, teacher, max_student) values('영어2', '홍영어', 100);

truncate student;
INSERT INTO student(name, phone, age, class) values('구영호', '01029091234', 27, '체육1');
INSERT INTO student(name, phone, age, class) values('서강일', '01029765432', 21, '국어1');
INSERT INTO student(name, phone, age, class) values('오선생', '01029083072', 27, '수학2');
INSERT INTO student(name, phone, age, class) values('김학생', '01012345678', 20, '수학1');
INSERT INTO student values('현공부', '01033201238', 21, '영어2');


select * from student join class on student.class=class.title

select * from student s join class c on s.class=c.title

select student.name, student.age, class.teacher from student join class on student.class=class.title

select s.name, s.age, c.teacher from student s join class c on s.class=c.title

select s.*, c.teacher from student s join class c on s.class=c.title

--김학생의 수업 과목을 담당하 선생님의 이름은?
select s.name, s.class, c.teacher from student s join class c on s.class=c.title where s.name='김학생'

-- 나이가 25세 미만인 학생들이 듣는 수업을 담당하는 선생님들 이름을 내림차순으로 가져올 것?
select s.name, s.class, c.teacher from student s join class c on s.class=c.title where s.age < 25 order by c.teacher desc


select * from class

INSERT INTO student(name, phone, age, class) values('장경필', '01029093234', 27, '체육1');
INSERT INTO student(name, phone, age, class) values('손조용', '01093802483', 28, '국어1');
INSERT INTO student(name, phone, age, class) values('강영우', '01046305652', 30, '수학2');
INSERT INTO student(name, phone, age, class) values('양귀비', '01057396760', 28, '수학1');
INSERT INTO student(name, phone, age, class) values('우종식', '01099975541', 22, '물리1');
INSERT INTO student(name, phone, age, class) values('연남길', '01000986421', 19, '수학1');
INSERT INTO student(name, phone, age, class) values('조용한', '01033320001', 50, '체육1');

--최대 정원의 최대값
select max(max_student) from class

select min(max_student) from class

--최대 정원 모두 더하기
select sum(max_student) from class

--평균 최대 정원
select avg(max_student) from class

--총 레코드 갯수
select count(*) from class;
select count(*) from student;

--수업별  최연장자
select class, max(age) from student s group by class;
select class, min(age) from student s group by class;

--수업별 연령평균
select class, avg(age) from student s group by class;

--수업별 학생수
select class, count(*) from student s group by class;

--Join + aggregation
select c.teacher, count(*) from student s join class c on s.class = c.title group by c.teacher;
select c.teacher, count(*) c from student s join class c on s.class = c.title group by c.teacher order by c desc, c.teacher asc;

