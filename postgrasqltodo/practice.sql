create table employ(
  emp_id SERIAL not null PRIMARY KEY,
  name varchar(100),
  lastName varchar(100),
  email varchar(100) not null UNIQUE,
  dept varchar(100),
  salary decimal(10,3) default 30000.00,
  hiredate Date not null default current_date
);


INSERT INTO employ (name, lastName, email, dept, salary, hiredate) VALUES
('Rahul', 'Sharma', 'rahul.sharma1@example.com', 'IT', 45000.500, '2023-01-15'),
('Priya', 'Verma', 'priya.verma2@example.com', 'HR', 38000.000, '2022-11-20'),
('Amit', 'Kumar', 'amit.kumar3@example.com', 'Finance', 52000.750, '2021-07-10'),
('Sneha', 'Patel', 'sneha.patel4@example.com', 'Marketing', 41000.250, '2023-03-05'),
('Vikram', 'Singh', 'vikram.singh5@example.com', 'IT', 60000.000, '2020-09-18'),
('Anjali', 'Mehta', 'anjali.mehta6@example.com', 'Sales', 39000.300, '2022-05-22'),
('Rohit', 'Gupta', 'rohit.gupta7@example.com', 'IT', 47000.100, '2021-12-01'),
('Neha', 'Agarwal', 'neha.agarwal8@example.com', 'HR', 36000.900, '2023-06-14'),
('Karan', 'Malhotra', 'karan.malhotra9@example.com', 'Finance', 55000.000, '2019-08-30'),
('Pooja', 'Bansal', 'pooja.bansal10@example.com', 'Marketing', 42000.450, '2022-02-11'),
('Arjun', 'Reddy', 'arjun.reddy11@example.com', 'Sales', 39000.000, '2023-04-09'),
('Isha', 'Kapoor', 'isha.kapoor12@example.com', 'IT', 61000.800, '2020-10-25'),
('Manish', 'Yadav', 'manish.yadav13@example.com', 'Operations', 34000.000, '2021-06-19'),
('Divya', 'Nair', 'divya.nair14@example.com', 'Finance', 53000.200, '2018-12-12'),
('Siddharth', 'Joshi', 'siddharth.joshi15@example.com', 'IT', 48000.600, '2022-09-17'),
('Kavita', 'Iyer', 'kavita.iyer16@example.com', 'HR', 37000.000, '2023-07-01'),
('Nikhil', 'Chopra', 'nikhil.chopra17@example.com', 'Marketing', 44000.750, '2021-03-28'),
('Meera', 'Saxena', 'meera.saxena18@example.com', 'Sales', 39500.500, '2022-08-16'),
('Yash', 'Thakur', 'yash.thakur19@example.com', 'Operations', 33000.000, '2020-01-05'),
('Ritika', 'Deshmukh', 'ritika.deshmukh20@example.com', 'Finance', 51000.900, '2019-04-21');


select * from employ

-- clauses ---> FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT, LIKE, DISTINCT, IN , NOT IN

select * from employ where salary > 40000

select * from employ where salary >= 40000 or dept = 'IT'

SELECT * FROM employ 
WHERE dept = 'IT' AND salary > 30000;

SELECT * FROM employ 
WHERE dept != 'IT' AND salary > 30000;


SELECT * FROM employ 
WHERE dept IN('IT', 'HR') 

SELECT * FROM employ 
WHERE dept NOT  IN('IT', 'HR') 

-- BETWEEN lower_value AND higher_value
SELECT * FROM employ 
WHERE salary BETWEEN 40000 AND 50000 and dept='IT'; 

-- not between
SELECT * FROM employ
WHERE salary NOT BETWEEN 40000 AND 50000;

-- ya b not <> ki tarha work karta hain 
SELECT * FROM employ
WHERE dept <> 'IT';

-- jin ka nam a se start hota hoga 
SELECT * FROM employ
WHERE name LIKE 'A%';

-- jin ka nam a se start hota hoga  or ya bara A ho ya chota dono aye gay 
SELECT * FROM employ
WHERE name ILIKE 'a%';

-- (% Multiple characters )( _  Single character)
SELECT * FROM employ
WHERE name ILIKE '_a%';

SELECT * FROM employ
WHERE name ILIKE '_a_i%';

-- between a
SELECT * FROM employ
WHERE name ILIKE '_%a%';

-- givin duplicate value
select dept FROM employ 

-- UNIQUE value 
select DISTINCT dept from  employ

-- sort data
select * from employ order by name

-- reverse data sort
SELECT * FROM employ 
ORDER BY name DESC;

SELECT * FROM employ 
ORDER BY emp_id DESC

SELECT * FROM employ
ORDER BY dept ASC, salary DESC;

-- limit 
SELECT * FROM employ  limit 5

SELECT * FROM employ
ORDER BY emp_id DESC
LIMIT 5;

SELECT * FROM (
    SELECT * FROM employ
    ORDER BY emp_id DESC
    LIMIT 5
) sub
ORDER BY emp_id ASC;

-- skip first 5 rows, next 5 rows dikhao
SELECT * FROM employ
ORDER BY emp_id
LIMIT 5 OFFSET 5;

-- Aggregate Functions
SELECT COUNT(emp_id) FROM employ;

SELECT COUNT(*) AS total_employees FROM employ;

SELECT COUNT(DISTINCT dept) FROM employ;

SELECT SUM(salary) AS total_salary FROM employ;

SELECT AVG(salary) AS average_salary FROM employ;

SELECT MIN(salary) AS lowest_salary,
       MAX(salary) AS highest_salary
FROM employ;

-- group 
-- dept ka group bana deya 
select dept from employ GROUP BY dept  
-- dept main kitne employ hain ?
select dept, count(emp_id) from employ GROUP BY dept  

--Department-wise employee count + average salary
select dept, 
count(emp_id) as totalemploy,
AVG(salary) AS average_salary
from employ 
GROUP BY dept 

--Departments with more than 2 employees
--- *** HAVING → group ke upar condition lagata hai (WHERE nahi lagta aggregate pe)
select dept,
count(emp_id)
from employ
group by dept
having count(*) > 3

-- wo dept ki avg b 50k se zeyada ho 
SELECT dept, AVG(salary) AS avg_salary
FROM employ
GROUP BY dept
HAVING AVG(salary) > 50000;

SELECT dept, MIN(salary) AS min_salary, MAX(salary) AS max_salary
FROM employ
GROUP BY dept
HAVING MAX(salary) > 43000 AND MIN(salary) < 42000;


---length
select length(name) as namecount from employ
select * from employ where length(name) > 4

--string function
select concat(name,' ', lastname) as fullname from employ
-- concat with sparator
select concat_ws('----', name, lastname) as fullname from employ
select concat_ws('___', name, lastname) as fullname from employ
select concat_ws('==', name, lastname) as fullname from employ

select substr(name, 1,4) from employ
select name from employ

SELECT SUBSTRING(name FROM 3) FROM employ;

-- SUBSTRING(string FROM start_index FOR LENGTH(string) - start_index - (-end_if_negative) + 1)
SELECT SUBSTRING(name FROM 2 FOR (LENGTH(name) - 2 - 3 + 1)) AS result FROM employ;

-- Uppercase & Lowercase
SELECT name,
       UPPER(name) AS upper_name,
       LOWER(name) AS lower_name,
       INITCAP(name) AS initcap_name
FROM employ;

-- Substring / LEFT / RIGHT
SELECT name,
       SUBSTRING(name FROM 1 FOR 3) AS first_3_letters,
       LEFT(name, 2) AS left2,
       RIGHT(name, 2) AS right2
FROM employ;

-- Trim spaces
SELECT name,
       TRIM(BOTH ' ' FROM name) AS trimmed_name,
       LTRIM(name) AS ltrim_name,
       RTRIM(name) AS rtrim_name
FROM employ;

-- Replace characters
SELECT name,
       REPLACE(name,'a','@') AS replaced_name,
       REPLACE(lastName,'a','*') AS replaced_lastName
FROM employ;

-- Position of a character
SELECT name,
       POSITION('a' IN name) AS first_a_position
FROM employ;

-- Split email into username & domain
SELECT email,
       SPLIT_PART(email,'@',1) AS email_username,
       SPLIT_PART(email,'@',2) AS email_domain
FROM employ;

-- Overlay (replace substring at specific position)
SELECT name,
       OVERLAY(name PLACING 'XXX' FROM 2 FOR 3) AS overlay_name
FROM employ;

-- LPAD / RPAD jasy mujha 8 word chahiya ho lakin kuch word 5 ky hogay tu baki ky left/right se * lag jay gay
SELECT name,
       LPAD(name, 8, '*') AS left_padded,
       RPAD(name, 8, '*') AS right_padded
FROM employ;

-- ASCII / CHR
SELECT name,
       ASCII(SUBSTRING(name FROM 1 FOR 1)) AS ascii_first_letter,
       CHR(65) AS chr_65
FROM employ;

-- Regex replace example
SELECT email,
       REGEXP_REPLACE(email, '\d+', '') AS email_no_digits
FROM employ;

-- Regex match example
SELECT email,
       REGEXP_MATCHES(email, '[a-z]+') AS first_match_letters
FROM employ;

-- Reverse
select name, 
reverse(name) as reverse_name 
from employ

-- assigment
select concat_ws(':', emp_id , name, lastname, dept) from employ
select concat_ws(':', emp_id , concat(name,' ', lastname), dept, salary) from employ
select concat(LEFT(dept, 1), emp_id, name) from employ
SELECT * FROM employ ORDER BY salary ASC;
SELECT * FROM employ ORDER BY salary DESC;
SELECT * FROM employ limit 3
select * from employ where name ILIKE 'A%'
select * from employ where length(lastname) > 6
--assigment 2
select count(emp_id) from employ
select dept, count(emp_id) as eachDepartmentMember from employ 
group by dept 

select * from employ ORDER BY salary ASC limit 1

select * from employ 
where
salary=(select min(salary) from employ)

select dept, AVG(salary) from employ
group by dept

select sum(salary) from employ where dept='HR'

-- learning
ALTER TABLE employ ADD COLUMN age INT default  30
SELECT * FROM EMPLOY
ALTER TABLE employ DROP COLUMN age
SELECT * FROM EMPLOY

--CHANGE CLOUMN NAME
ALTER TABLE employ RENAME COLUMN NAME TO FIRSTNAME
SELECT * FROM EMPLOY
ALTER TABLE employ RENAME COLUMN FIRSTNAME TO NAME

-- CHANGE TABLE NAME
ALTER TABLE employ RENAME TO COMPANY_EMPLOY
SELECT * FROM COMPANY_EMPLOY

ALTER TABLE COMPANY_EMPLOY RENAME TO employ
SELECT * FROM EMPLOY

ALTER TABLE EMPLOY
ALTER COLUMN NAME 
SET DATA TYPE VARCHAR(80)

ALTER TABLE EMPLOY
ALTER COLUMN NAME 
SET DEFAULT 'UNKNOWN'

ALTER TABLE EMPLOY
ALTER COLUMN NAME 
DROP DEFAULT

ALTER TABLE EMPLOY
ALTER COLUMN NAME 
SET NOT NULL

ALTER TABLE EMPLOY
ALTER COLUMN NAME 
DROP NOT NULL

ALTER TABLE EMPLOY
ADD COLUMN PHONE VARCHAR(100)
CHECK (LENGTH(PHONE) = 11 OR LENGTH(PHONE) = 13 )

INSERT INTO employ (name, lastname, email, dept, salary, phone)
VALUES ('Ali','Khan','ali.kh7771@example.com','IT',35000,'0322378894567676757');

UPDATE employ
SET phone = '0322334'
WHERE emp_id = 3;

ALTER TABLE EMPLOY
DROP CONSTRAINT EMPLOY_PHONE_CHECK;
-- NOW WORK
UPDATE employ
SET phone = '0322334'
WHERE emp_id = 3;

ALTER TABLE EMPLOY
ADD CONSTRAINT MON_NUM_LESS_THEN_10
     CHECK (Length(phone) >= 10);

SELECT name, salary,
CASE 
    WHEN salary >= 50000 THEN 'HIGH'
    ELSE 'LOW'
END AS sal_cat
FROM employ;


SELECT name, salary,
CASE 
    WHEN salary >= 50000 THEN 'HIGH'
	WHEN salary >= 40000 AND salary <=50000 THEN 'mid'
    ELSE 'LOW'
END AS sal_cat
FROM employ;

SELECT name, salary,
CASE 
    WHEN salary > 0 THEN ROUND((salary / 10 ))
END AS bonus
FROM employ;


SELECT
CASE 
    WHEN salary >= 50000 THEN 'HIGH'
	WHEN salary >= 40000 AND salary <=50000 THEN 'mid'
    ELSE 'LOW'
END AS sal_cat,
count(emp_id)
FROM employ
GROUP BY sal_cat;





