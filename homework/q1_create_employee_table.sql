-- 이 파일을 제대로 작성하지 않거나, 오답일 경우 자동으로 Q2, Q5, Q6, Q9, Q10이 오답 처리됩니다.
-- Q1. employee 테이블을 생성하시오. 테이블의 스펙은 아래와 같습니다.
-- 1. emp_id는 알파벳(A~Z) 한 글자로 시작하며, 이후 5자리 숫자로 조합이 됩니다(e.g A00001), null 값이 올 수 없습니다. employee 테이블 내에서 고유한 값을 갖습니다.
-- 2. Gender는 Male, Female, Others로만 구성됩니다. null값이 올 수 없습니다.
-- 3. name은 최대 20자까지 허용이 되며, 영문 알파벳으로만 구성이 됩니다. null 값이 올 수 없습니다.
-- 4. address는 최대 100자까지 허용이 되며, 영문 알파벳과 쉼표, dash(-), 숫자, 공백(space)로 구성이됩니다. null 값이 허용이 됩니다.
-- 5. department는 숫자형입니다. 값은 100미만입니다. null값이 허용이 됩니다
-- 6. manager는 emp_id 값으로 해당 직원의 매니저의 emp_id값입니다. 제약 사항은 emp_id와 동일하나, null값이 허용이 됩니다. 여러 레코드가 같은 manager일 수 있으며, 따라서 중복이 허용됩니다
-- 7. age는 숫자형으로 200미만  숫자로 null값이 올 수 없습니다.
-- 8. Position은 최대 30자까지 올 수 있으며, null값이 허용이 됩니다.

create table employee(
    emp_id varchar(10) primary key not null,
    gender varchar(10) not null,
    name varchar(20) not null,
    address varchar(100),
    department int,
    manager varchar(10),
    age int,
    Position varchar(30)
)