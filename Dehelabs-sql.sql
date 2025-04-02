/* Table: Department */
create table Departments(
department_id INT NOT NULL auto_increment,
department_name Varchar(50) NOT NULL,
primary key (department_id)
);

/* Table: Employees */
create table Employees(
employee_id INT NOT NULL auto_increment,
name Varchar(50) NOT NULL,
salary decimal(10,2) not null,
department_id int,
manager_id int ,
foreign key (department_id) references Departments (department_id),
foreign key (manager_id) references Employees (employee_id),
primary key (employee_id)
);

/* Drop Table Employees; */

/* Table: Customers */
create table customers(
customer_id int not null,
customer_name Varchar(50) not null,
email Varchar(100) Unique not null,
primary key (customer_id)
);

/* Table: Products */
create Table Products(
product_id int not null,
product_name Varchar(50) not null,
price decimal(10,2) not null,
primary key (product_id)
);

/* Table: Orders */
create Table Orders(
order_id int not null,
customer_id int not null,
order_date date not null,
foreign key (customer_id) references customers (customer_id),
primary key (order_id)
);

/* Table: Orderdetails */
create Table Orderdetails(
order_detail_id int not null,
order_id int not null,
product_id int not null,
quantity int not null check (quantity>0),
foreign key (order_id) references Orders (order_id),
foreign key (product_id) references Products (product_id),
primary key (order_detail_id)
);


/* Data for Departments */
Insert into Departments (department_id,department_name) values 
(1,"HR"),
(2,"Engineering"),
(3,"Sales"),
(4,"Marketing");

/* Data for Employees */
Insert into Employees (employee_id,name,salary,department_id,manager_id) values
(101,"Alice Johnson",60000,1,Null),
(102,"Bob smith",75000,2,Null),
(103,"Charlie Brown",50000,2,102),
(104,"David Willam",90000,3,Null),
(105,"Emma Davis", 45000,3,104),
(106,"Frank Miller",40000,3,104),
(107,"Grace Willson",70000,4,Null);

/* Data for customers */
Insert into customers (customer_id,customer_name,email) values
(1,"John Doe","john.doe@gmail.com"),
(2,"Jane smith","jane.smith@yahoo.com"),
(3,"Michael Brown","michael.b@gmail.com"),
(4,"Emily white","emily.white@outlook.com"),
(5,"Robert Green","robert.green@gmail.com");

/* Data for products */
Insert into Products (product_id,product_name,price) values
(1,"Laptop",80000),
(2,"Smartphone",45000),
(3,"Headphone",5000),
(4,"Smartwatch",12000),
(5,"Tablet",30000);

/* Data for Orders */
Insert into Orders (order_id,customer_id,order_date) values
(101,1,"2024-03-01"),
(102,2,"2024-03-02"),
(103,1,"2024-03-05"),
(104,3,"2024-03-07"),
(105,4,"2024-03-10");

/* Data for Orderdetails*/
Insert into Orderdetails (order_detail_id,order_id,product_id,quantity) values 
(1,101,1,1),
(2,101,3,2),
(3,102,2,1),
(4,103,5,1),
(5,104,4,1),
(6,105,3,1);

select * from Departments;
select * from Employees;
select * from customers;
select * from Products;
select * from Orders;
select * from Orderdetails;

/* Excercise questions -- Basic Queries (SELECT, WHERE, GROUP BY, ORDER BY) */
/* Retrieve all employees who earn more than 50,000. */
select * from Employees where salary>50000;

/* List all customers whose email contains "gmail.com". */
select * from customers where email like "%gmail.com%";

/* Get the total number of orders placed by each customer.*/
select customer_id,COUNT(Order_id) as Total_orders from orders  group by customer_id;

/* Show all products that cost more than 500 sorted by price in descending order. */
select * from Products where price>500 order by price desc;

/* Find the total revenue generated from all sales. */
select sum(od.quantity*P.price) as total_revenue from 
Orderdetails od
join
Products P
on od.product_id=P.product_id; 

/* Joins (INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN) */
/* Retrieve the names of employees along with their department names. */
select (E.name) as Employee_name,D.department_name
from
Employees E
Left join
Departments D 
on E.department_id=D.department_id;

/* Get a list of all customers who have never placed an order.*/
select C.customer_name
from 
customers C
left join
Orders O
on C.customer_id=O.customer_id where O.order_id is Null;

/* Show all products along with the number of times they have been ordered.*/
select P.product_name,sum(Od.quantity) as no_of_times_ordered
from 
Products P
left join
Orderdetails Od
on P.product_id = Od.product_id group by P.product_name;

/* Display all orders along with customer names and the total order amount.*/
select C.customer_name,sum(P.price*Od.quantity) as total_order_amount
from customers C
join
Orders O
on C.customer_id=O.customer_id
join
Orderdetails Od
on O.order_id=Od.order_id
join
Products P
on P.product_id=Od.product_id
group by C.customer_name;

/* Find employees who do not have a manager.*/
select A.name
from Employees A
join
Employees B
on A.employee_id=B.employee_id where A.manager_id is Null; 

/* Aggregate Functions (SUM, COUNT, AVG, MIN, MAX)*/
/* Count the total number of employees in each department.*/
select count(employee_id) as total_number_of_employees 
from Employees
group by department_id;

/*Find the department with the highest average salary.*/
select D.department_id,D.department_name,AVG(E.salary) as Average_salary
from Employees E
join
Departments D
on E.department_id=D.department_id
group by D.department_name order by Average_salary desc limit 1 ;

/* Get the total number of products sold (sum of all quantities).*/
select sum(quantity) as total_number_of_products_sold 
from Orderdetails;

/* Find the highest order amount placed by a single customer.*/
select Max(P.price*Od.quantity) as highest_order_amount
from Products P
join
Orderdetails Od
on P.product_id=Od.product_id ;

/* Find the average salary of employees who work in the "Sales" department.*/
select E.name,AVG(E.salary)
from Employees E
join
Departments D
on E.department_id=D.department_id
where D.department_name="sales";

/* Window Functions (RANK, DENSE_RANK, ROW_NUMBER, LEAD, LAG) */
/* Rank employees in each department based on their salaries.*/
select E.name,D.department_name,
Rank() OVER(partition by D.department_name order by E.salary desc) as Emp_rank
from Employees E
join
Departments D
on E.department_id=D.department_id;

/* Find the cumulative revenue per order (running total). */
select Od.order_id,SUM(P.price*Od.quantity),
SUM(SUM(P.price*Od.quantity)) over (order by Od.order_id) as running_total
from Products P
join
Orderdetails Od
on P.product_id=Od.product_id
group by Od.order_id;

/* Assign a unique row number to each employee in each department.*/
select E.name,D.department_name,
ROW_NUMBER() OVER(order by D.department_name) as new_row_number
from Departments D
join
Employees E
on D.department_id=E.department_id
order by D.department_name;

/* Find the previous order amount for each order placed.*/
select Od.order_id,SUM(P.price*Od.quantity),
LAG(SUM(P.price*Od.quantity)) OVER (order by Od.order_id) as previous_order_amount
from Products P
join
Orderdetails Od
on P.product_id=Od.product_id
group by Od.order_id;

/* Get the top 3 highest-earning employees in each department.*/
select E.employee_id,E.name,D.department_name,E.salary,
RANK() OVER(partition by D.department_id order by E.salary desc) as Highest_earning_salary
from Departments D
join
Employees E
on D.department_id=E.department_id
order by D.department_id;

/* Subqueries & Nested Queries */
/* Find the second highest salary from the Employees table.*/
select Max(salary)
 from Employees 
 where salary < (select Max(salary) from Employees);
 
 /* Retrieve the names of departments where the average employee salary is more than 70,000. */
 select department_name from Departments where department_id IN (
 select department_id from Employees group by department_id HAVING AVG(salary)>40000.00);
 
 /* Get a list of customers who have ordered more than 5 times.*/
 select customer_name from customers where customer_id in (
 select customer_id from Orders  having Count(order_id)>3);
 
 /* Find employees whose salary is greater than the average salary of their department. */
select e.name from Employees e where e.salary>(select AVG(salary) from Employees
where department_id = e.department_id);
 
 /* Retrieve all employees who earn more than their own manager.*/
 select name from Employees e  where salary >(select salary from Employees where employee_id=e.manager_id);
 
/* update Employees set salary=1000 where employee_id=102;*/

/* ------------------------------------------------------------------------------------------------------------------------------*/
/* String Function*/
create table Employees1(
emp_id int not null auto_increment,
first_name varchar(50) not null,
last_name varchar(50) not null,
department varchar(20) not null,
primary key (emp_id)
);

Insert into Employees1  (first_name,last_name,department) values 
("john","doe","HR"),
("alice","smith","IT"),
("bob","brown","Finance"),
("charlie","wilson","HR");

create table Users(
user_id int not null auto_increment,
email varchar(50) unique not null,
primary key (user_id)
);

Insert into Users (email) values ("john.doe@gmail.com"),
("alice_smith@gmail.com"),
("bob123@outlook.com"),
("charlie@company.org");

create table Messages(
msg_id int not null auto_increment,
text_message Varchar(50) not null,
primary key (msg_id)
);

Insert into Messages (text_message) values
("Hello World"),
("SQL is Powerfull"),
("Data science rocks"),
("String functions");

create table Customers1(
cust_id int not null auto_increment,
full_name Varchar(50) not null,
primary key (cust_id)
);

Insert into Customers1 (full_name) values
("John Doe"),
("Alice Smith"),
("Bob Brown"),
("Charlie Wilson");

create table Pad_account_number(
acc_id int not null auto_increment,
account_number int not null,
primary key (acc_id)
);

Insert into Pad_account_number (account_number) Values
(12345),
(6789),
(456),
(98765);

create table Feedback(
feedback_id int not null auto_increment,
comments varchar(100) not null,
primary key (feedback_id)
);

Insert into Feedback (comments) values
("This Product is Bad"),
("Bad service experience"),
("Not a bad choice"),
("Bad quality issue");

create table Sentences(
sentence_id int not null auto_increment,
texts Varchar(50) not null,
primary key (sentence_id)
);

Insert into Sentences (texts) values 
("Banana is fruit"),
("Amazing Apple pie"),
("Always be happy"),
("All about Analytics");

create Table Authors(
author_id int not null auto_increment,
name Varchar(50) not null,
primary key (author_id)
);

Insert into Authors (name) values
("J.K.Rowling"),
("George R.R.Martin"),
("Agatha Christie"),
("William Shakespeare");

create table Products1(
product_id int not null auto_increment,
product_name Varchar(50) not null,
primary key (product_id)
);

Insert into Products1 (product_name) values
(" Apple "),
(" Banana "),
(" Mango "),
(" Grapes ");



select * from Employees1;
select * from Users;
select * from Messages;
select * from Customers1;
select * from Pad_account_number;
select * from Feedback;
select * from Sentences;
select * from Authors;
select * from Products1;

/* Write an SQL query to concatenate first_name and last_name with a space in between and convert them into proper case (first letter capitalized).*/
select CONCAT(UPPER(LEFT(first_name,1)),LOWER(SUBSTRING(first_name,2))," ",last_name) as Full_name from Employees1; 

/*Extract Domain from Emails */
select email,SUBSTRING_INDEX(email,"@",-1) as domain_name from Users;

/* Write a query to find all employees whose first name contains the letter "a" (case insensitive).*/
select * from Employees1 where first_name like "a%";

/* Write an SQL query to reverse the text in the text_message column.*/
select text_message,reverse(text_message) as reverse_text from Messages;

/* Extract and display the initials (first letter of first name + first letter of last name) for each customer.*/
select full_name,CONCAT(LEFT(full_name,1),LEFT(SUBSTRING_INDEX(full_name," ",-1),1)) as Initials
from Customers1;

/* Write a query to ensure that all account_number values are padded with leading zeros to make them 8 characters long.*/
select account_number,LPAD(account_number,8,0) as padded_account_number from Pad_account_number;

/* Replace all occurrences of the word "bad" with "poor" in the comment column.*/
select comments,REPLACE(comments,"Bad","Poor") as Updated_comments from Feedback;

/* Count how many times the letter 'a' appears in each sentence.*/
select texts,LENGTH(Lower(texts))-LENGTH(REPLACE(LOWER(texts),'a','')) as count_a
from Sentences;

/* Split Full Name into First and Last Name */
select full_name,SUBSTRING_INDEX(full_name," ",1) as first_name,
SUBSTRING_INDEX(full_name," ",-1) as last_name
from Customers1;

/* Find Longest Name */
select name,MAX(LENGTH(name)) as length_of_name from Authors; 

/* Write an SQL query to remove any leading and trailing spaces from the product_name column.*/
select product_id,TRIM(product_name) as product_name_cleaned from Products1;


create table Employees2(
emp_id int not null auto_increment,
first_name Varchar(50) not null,
dob date not null,
primary key (emp_id)
);

Insert into Employees2 (first_name,dob) values 
("John","1990-05-15"),
("Alice","1985-10-22"),
("Bob","1998-07-09"),
("Charlie","2000-12-01");

select * from Employees2;

/* Write an SQL query to calculate the age of each employee as of today.*/
select emp_id,first_name,
TIMESTAMPDIFF(YEAR,dob,CURDATE()) as AGE from Employees2;

CREATE TABLE Employees3 (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    joining_date DATE
);

INSERT INTO Employees3 VALUES
(1, 'John', '2024-01-10'),
(2, 'Alice', '2024-02-25'),
(3, 'Bob', '2023-12-30'),
(4, 'Charlie', '2024-03-15');

CREATE TABLE Orders1 (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    order_date DATE
);

INSERT INTO Orders1 VALUES
(1, 'John', '2023-01-15'),
(2, 'Alice', '2023-05-22'),
(3, 'Bob', '2024-02-10'),
(4, 'Charlie', '2024-03-01');

CREATE TABLE Rentals (
    rental_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    rental_start DATE,
    rental_end DATE
);

INSERT INTO Rentals VALUES
(1, 'John', '2024-03-01', '2024-03-10'),
(2, 'Alice', '2024-02-15', '2024-03-01'),
(3, 'Bob', '2024-01-10', '2024-02-10'),
(4, 'Charlie', '2024-03-05', '2024-03-20');

CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    transaction_date DATE
);

INSERT INTO Transactions VALUES
(1, 'John', '2024-03-02'),
(2, 'Alice', '2024-03-15'),
(3, 'Bob', '2024-03-20'),
(4, 'Charlie', '2024-03-31');

CREATE TABLE SystemInfo (
    log_id INT PRIMARY KEY,
    event_name VARCHAR(50),
    event_date TIMESTAMP
);

INSERT INTO SystemInfo VALUES
(1, 'System Boot', '2024-03-10 08:00:00'),
(2, 'User Login', '2024-03-10 09:15:30'),
(3, 'File Upload', '2024-03-10 10:30:00'),
(4, 'System Shutdown', '2024-03-10 23:00:00');

CREATE TABLE Events (
    event_id INT PRIMARY KEY,
    event_name VARCHAR(50),
    event_date DATE
);

INSERT INTO Events VALUES
(1, 'Conference', '2024-03-04'),
(2, 'Meeting', '2024-03-07'),
(3, 'Workshop', '2024-03-15'),
(4, 'Training', '2024-03-20');

select * from Employees3;
select * from Orders1;
select * from Rentals;
select * from Transactions;
select * from systemInfo;
select * from Employees2;
select * from Events;

/* Write a query to find employees who joined in the last 3 months. */
select emp_id,first_name,joining_date
from Employees3 
where joining_date>=DATE_SUB(CURDATE(),INTERVAL 3 month);

/* Write a query to extract the year and month from the order_date column. */
select order_id,customer_name,YEAR(order_date) as order_year,
MONTH(order_date) as order_month from Orders1;

/* Write a query to calculate the number of days between rental_start and rental_end for each customer.*/
select customer_name,datediff(rental_end,rental_start) as rental_duration
from Rentals;

/* Write a query to find all orders placed on a Saturday or Sunday. */
select order_id,customer_name
from Orders1 where WEEKDAY(order_date) IN (5,6);

/* Write an SQL query to find the first and last day of the current month. */
select date_format(CURDATE(),'%Y-%m-01') as first_day_month,
LAST_DAY(CURDATE()) as Last_day_month from Transactions;

/* Add 30 Days to a Given Date */
select order_date,date_add(order_date, INTERVAL 30 DAY) as new_date
from Orders1;

/* Write a query to get the current date and time. */
select NOW() as current_date_time;

/*  Find Employees Whose Birthday is This Month*/
select first_name from Employees2
where MONTH(dob)=MONTH(CURDATE());

