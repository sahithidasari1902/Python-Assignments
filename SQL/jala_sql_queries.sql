-- =====================================================================
-- JALA Academy - SQL Assignment
-- Tables: SALESPEOPLE, CUST, ORDERS  +  all 89 queries
-- Written for MySQL 8 (also works in MariaDB).
-- Run the whole file in MySQL Workbench: File > Open SQL Script,
-- then click the lightning-bolt icon (Execute).
-- =====================================================================

CREATE DATABASE IF NOT EXISTS jala_sql;
USE jala_sql;

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS cust;
DROP TABLE IF EXISTS salespeople;

-- ---------------------------------------------------------------------
-- TABLE CREATION
-- ---------------------------------------------------------------------
CREATE TABLE salespeople (
    snum   INT PRIMARY KEY,
    sname  VARCHAR(20) NOT NULL,
    city   VARCHAR(20),
    comm   DECIMAL(4,2)
);

CREATE TABLE cust (
    cnum    INT PRIMARY KEY,
    cname   VARCHAR(20) NOT NULL,
    city    VARCHAR(20),
    rating  INT,
    snum    INT,
    FOREIGN KEY (snum) REFERENCES salespeople(snum)
);

CREATE TABLE orders (
    onum   INT PRIMARY KEY,
    amt    DECIMAL(10,2),
    odate  DATE,
    cnum   INT,
    snum   INT,
    FOREIGN KEY (cnum) REFERENCES cust(cnum),
    FOREIGN KEY (snum) REFERENCES salespeople(snum)
);

-- ---------------------------------------------------------------------
-- DATA
-- ---------------------------------------------------------------------
INSERT INTO salespeople VALUES
(1001, 'Peel',    'London',    0.12),
(1002, 'Serres',  'San Jose',  0.13),
(1004, 'Motika',  'London',    0.11),
(1007, 'Rafkin',  'Barcelona', 0.15),
(1003, 'Axelrod', 'New York',  0.10);

-- NOTE: The assignment's ORDERS table uses customer 2008, and query 52
-- asks for customer "Cisneros", but 2008 is missing from the CUST table
-- in the document. It is added here (standard version of this dataset)
-- so the foreign keys and those queries work.
INSERT INTO cust VALUES
(2001, 'Hoffman',  'London',   100, 1001),
(2002, 'Giovanne', 'Rome',     200, 1003),
(2003, 'Liu',      'San Jose', 300, 1002),
(2004, 'Grass',    'Berlin',   100, 1002),
(2006, 'Clemens',  'London',   300, 1007),
(2007, 'Pereira',  'Rome',     100, 1004),
(2008, 'Cisneros', 'San Jose', 300, 1007);

-- Dates are stored in MySQL format YYYY-MM-DD ('03-OCT-94' = '1994-10-03')
INSERT INTO orders VALUES
(3001,   18.69, '1994-10-03', 2008, 1007),
(3003,  767.19, '1994-10-03', 2001, 1001),
(3002, 1900.10, '1994-10-03', 2007, 1004),
(3005, 5160.45, '1994-10-03', 2003, 1002),
(3006, 1098.16, '1994-10-04', 2008, 1007),
(3009, 1713.23, '1994-10-04', 2002, 1003),
(3007,   75.75, '1994-10-05', 2004, 1002),
(3008, 4723.00, '1994-10-05', 2006, 1001),
(3010, 1309.95, '1994-10-06', 2004, 1002),
(3011, 9891.88, '1994-10-06', 2006, 1001);

-- =====================================================================
-- QUERIES
-- =====================================================================

-- Q1. Display snum,sname,city and comm of all salespeople.
SELECT snum, sname, city, comm
FROM salespeople;

-- Q2. Display all snum without duplicates from all orders.
SELECT DISTINCT snum
FROM orders;

-- Q3. Display names and commissions of all salespeople in london.
SELECT sname, comm
FROM salespeople
WHERE city = 'London';

-- Q4. All customers with rating of 100.
SELECT *
FROM cust
WHERE rating = 100;

-- Q5. Produce orderno, amount and date form all rows in the order table.
SELECT onum, amt, odate
FROM orders;

-- Q6. All customers in San Jose, who have rating more than 200.
SELECT *
FROM cust
WHERE city = 'San Jose' AND rating > 200;

-- Q7. All customers who were either located in San Jose or had a rating above 200.
SELECT *
FROM cust
WHERE city = 'San Jose' OR rating > 200;

-- Q8. All orders for more than $1000.
SELECT *
FROM orders
WHERE amt > 1000;

-- Q9. Names and citires of all salespeople in london with commission above 0.10.
SELECT sname, city
FROM salespeople
WHERE city = 'London' AND comm > 0.10;

-- Q10. All customers excluding those with rating <= 100 unless they are located in Rome.
-- Keep customers with rating above 100, plus anyone in Rome.
SELECT *
FROM cust
WHERE rating > 100 OR city = 'Rome';

-- Q11. All salespeople either in Barcelona or in london.
SELECT *
FROM salespeople
WHERE city IN ('Barcelona', 'London');

-- Q12. All salespeople with commission between 0.10 and 0.12. (Boundary values should be excluded)
-- BETWEEN includes the boundaries, so use > and < instead.
SELECT *
FROM salespeople
WHERE comm > 0.10 AND comm < 0.12;

-- Q13. All customers with NULL values in city column.
-- NULL can't be compared with =, always use IS NULL.
SELECT *
FROM cust
WHERE city IS NULL;

-- Q14. All orders taken on Oct 3Rd   and Oct 4th  1994.
SELECT *
FROM orders
WHERE odate IN ('1994-10-03', '1994-10-04');

-- Q15. All customers serviced by peel or Motika.
SELECT c.cnum, c.cname, s.sname
FROM cust c
JOIN salespeople s ON c.snum = s.snum
WHERE s.sname IN ('Peel', 'Motika');

-- Q16. All customers whose names begin with a letter from A to B.
SELECT *
FROM cust
WHERE cname LIKE 'A%' OR cname LIKE 'B%';

-- Q17. All orders except those with 0 or NULL value in amt field.
-- Both conditions must be true, so AND (not OR).
SELECT *
FROM orders
WHERE amt IS NOT NULL AND amt <> 0;

-- Q18. Count the number of salespeople currently listing orders in the order table.
SELECT COUNT(DISTINCT snum) AS salespeople_with_orders
FROM orders;

-- Q19. Largest order taken by each salesperson, datewise.
SELECT snum, odate, MAX(amt) AS largest_order
FROM orders
GROUP BY snum, odate
ORDER BY snum, odate;

-- Q20. Largest order taken by each salesperson with order value more than $3000.
-- HAVING filters groups after GROUP BY (WHERE filters rows before).
SELECT snum, odate, MAX(amt) AS largest_order
FROM orders
GROUP BY snum, odate
HAVING MAX(amt) > 3000
ORDER BY snum, odate;

-- Q21. Which day had the hightest total amount ordered.
SELECT odate, SUM(amt) AS total_amount
FROM orders
GROUP BY odate
ORDER BY total_amount DESC
LIMIT 1;

-- Q22. Count all orders for Oct 3rd.
SELECT COUNT(*) AS orders_on_oct3
FROM orders
WHERE odate = '1994-10-03';

-- Q23. Count the number of different non NULL city values in customers table.
-- COUNT(column) ignores NULLs automatically; DISTINCT removes repeats.
SELECT COUNT(DISTINCT city) AS different_cities
FROM cust;

-- Q24. Select each customer's smallest order.
SELECT cnum, MIN(amt) AS smallest_order
FROM orders
GROUP BY cnum;

-- Q25. First customer in alphabetical order whose name begins with G.
SELECT MIN(cname) AS first_customer
FROM cust
WHERE cname LIKE 'G%';

-- Q26. Get the output like " For dd/mm/yy there are ___ orders.
SELECT CONCAT('For ', DATE_FORMAT(odate, '%d/%m/%y'),
              ' there are ', COUNT(*), ' orders.') AS result
FROM orders
GROUP BY odate;

-- Q27. Assume that each salesperson has a 12% commission. Produce order no., salesperson no., and amount of salesperson's commission for that order.
SELECT onum, snum, amt, amt * 0.12 AS commission
FROM orders;

-- Q28. Find highest rating in each city. Put the output in this form. For the city (city), the highest rating is : (rating).
SELECT CONCAT('For the city ', city, ', the highest rating is : ',
              MAX(rating)) AS result
FROM cust
GROUP BY city;

-- Q29. Display the totals of orders for each day and place the results in descending order.
SELECT odate, SUM(amt) AS total_amount
FROM orders
GROUP BY odate
ORDER BY total_amount DESC;

-- Q30. All combinations of salespeople and customers who shared a city. (ie same city).
SELECT s.sname, c.cname, s.city
FROM salespeople s
JOIN cust c ON s.city = c.city;

-- Q31. Name of all customers matched with the salespeople serving them.
SELECT c.cname, s.sname
FROM cust c
JOIN salespeople s ON c.snum = s.snum;

-- Q32. List each order number followed by the name of the customer who made the order.
SELECT o.onum, c.cname
FROM orders o
JOIN cust c ON o.cnum = c.cnum;

-- Q33. Names of salesperson and customer for each order after the order number.
SELECT o.onum, s.sname, c.cname
FROM orders o
JOIN cust c        ON o.cnum = c.cnum
JOIN salespeople s ON o.snum = s.snum;

-- Q34. Produce all customer serviced by salespeople with a commission above 12%.
SELECT c.cname, s.sname, s.comm
FROM cust c
JOIN salespeople s ON c.snum = s.snum
WHERE s.comm > 0.12;

-- Q35. Calculate the amount of the salesperson's commission on each order with a rating above 100.
SELECT o.onum, s.sname, c.cname, c.rating,
       o.amt * s.comm AS commission
FROM orders o
JOIN cust c        ON o.cnum = c.cnum
JOIN salespeople s ON o.snum = s.snum
WHERE c.rating > 100;

-- Q36. Find all pairs of customers having the same rating.
-- SELF JOIN: the same table used twice with two aliases (a and b).
SELECT a.cname, b.cname, a.rating
FROM cust a
JOIN cust b ON a.rating = b.rating
WHERE a.cnum <> b.cnum;

-- Q37. Find all pairs of customers having the same rating, each pair coming once only.
-- a.cnum < b.cnum keeps (A,B) but drops the reversed (B,A).
SELECT a.cname, b.cname, a.rating
FROM cust a
JOIN cust b ON a.rating = b.rating
WHERE a.cnum < b.cnum;

-- Q38. Policy is to assign three salesperson to each customers. Display all such combinations.
-- Every customer combined with every group of 3 different salespeople.
SELECT c.cname, s1.sname AS sales1, s2.sname AS sales2, s3.sname AS sales3
FROM cust c
CROSS JOIN salespeople s1
CROSS JOIN salespeople s2
CROSS JOIN salespeople s3
WHERE s1.snum < s2.snum AND s2.snum < s3.snum
ORDER BY c.cname;

-- Q39. Display all customers located in cities where salesman serres has customer.
SELECT *
FROM cust
WHERE city IN (SELECT c.city
               FROM cust c
               JOIN salespeople s ON c.snum = s.snum
               WHERE s.sname = 'Serres');

-- Q40. Find all pairs of customers served by single salesperson.
SELECT a.cname, b.cname, a.snum
FROM cust a
JOIN cust b ON a.snum = b.snum
WHERE a.cnum < b.cnum;

-- Q41. Produce all pairs of salespeople which are living in the same city. Exclude combinations of salespeople with themselves as well as duplicates with the order reversed.
SELECT a.sname, b.sname, a.city
FROM salespeople a
JOIN salespeople b ON a.city = b.city
WHERE a.snum < b.snum;

-- Q42. Produce all pairs of orders by given customer, names that customers and eliminates duplicates.
SELECT c.cname, a.onum, b.onum
FROM orders a
JOIN orders b ON a.cnum = b.cnum
JOIN cust c   ON c.cnum = a.cnum
WHERE a.onum < b.onum;

-- Q43. Produce names and cities of all customers with the same rating as Hoffman.
SELECT cname, city
FROM cust
WHERE rating = (SELECT rating FROM cust WHERE cname = 'Hoffman')
  AND cname <> 'Hoffman';

-- Q44. Extract all the orders of Motika.
SELECT *
FROM orders
WHERE snum = (SELECT snum FROM salespeople WHERE sname = 'Motika');

-- Q45. All orders credited to the same salesperson who services Hoffman.
SELECT *
FROM orders
WHERE snum = (SELECT snum FROM cust WHERE cname = 'Hoffman');

-- Q46. All orders that are greater than the average for Oct 4.
SELECT *
FROM orders
WHERE amt > (SELECT AVG(amt) FROM orders WHERE odate = '1994-10-04');

-- Q47. Find average commission of salespeople in london.
SELECT AVG(comm) AS avg_comm_london
FROM salespeople
WHERE city = 'London';

-- Q48. Find all orders attributed to salespeople servicing customers in london.
SELECT *
FROM orders
WHERE snum IN (SELECT snum FROM cust WHERE city = 'London');

-- Q49. Extract commissions of all salespeople servicing customers in London.
SELECT sname, comm
FROM salespeople
WHERE snum IN (SELECT snum FROM cust WHERE city = 'London');

-- Q50. Find all customers whose cnum is 1000 above the snum of serres.
SELECT cnum, cname
FROM cust
WHERE cnum > (SELECT snum + 1000 FROM salespeople WHERE sname = 'Serres');

-- Q51. Count the customers with rating  above San Jose's average.
SELECT COUNT(*) AS customers_above_sj_avg
FROM cust
WHERE rating > (SELECT AVG(rating) FROM cust WHERE city = 'San Jose');

-- Q52. Obtain all orders for the customer named Cisnerous. (Assume you don't know his customer no. (cnum)).
SELECT *
FROM orders
WHERE cnum = (SELECT cnum FROM cust WHERE cname = 'Cisneros');

-- Q53. Produce the names and rating of all customers who have above average orders.
SELECT DISTINCT c.cname, c.rating
FROM cust c
JOIN orders o ON c.cnum = o.cnum
WHERE o.amt > (SELECT AVG(amt) FROM orders);

-- Q54. Find total amount in orders for each salesperson for whom this total is greater than the amount of the largest order in the table.
SELECT snum, SUM(amt) AS total_amount
FROM orders
GROUP BY snum
HAVING SUM(amt) > (SELECT MAX(amt) FROM orders);

-- Q55. Find all customers with order on 3rd Oct.
SELECT DISTINCT c.*
FROM cust c
JOIN orders o ON c.cnum = o.cnum
WHERE o.odate = '1994-10-03';

-- Q56. Find names and numbers of all salesperson who have more than one customer.
SELECT s.snum, s.sname, COUNT(c.cnum) AS customers
FROM salespeople s
JOIN cust c ON s.snum = c.snum
GROUP BY s.snum, s.sname
HAVING COUNT(c.cnum) > 1;

-- Q57. Check if the correct salesperson was credited with each sale.
-- Compare the salesperson on the order with the customer's assigned one.
SELECT o.onum, o.cnum, o.snum AS credited_snum, c.snum AS assigned_snum,
       CASE WHEN o.snum = c.snum THEN 'Correct' ELSE 'Wrong' END AS status
FROM orders o
JOIN cust c ON o.cnum = c.cnum;

-- Q58. Find all orders with above average amounts for their customers.
-- CORRELATED subquery: the inner query uses a.cnum from the outer row.
SELECT *
FROM orders a
WHERE amt > (SELECT AVG(b.amt) FROM orders b WHERE b.cnum = a.cnum);

-- Q59. Find the sums of the amounts from order table grouped by date, eliminating all those dates where the sum was not at least 2000 above the maximum amount.
SELECT odate, SUM(amt) AS total_amount
FROM orders
GROUP BY odate
HAVING SUM(amt) >= (SELECT MAX(amt) FROM orders) + 2000;

-- Q60. Find names and numbers of all customers with ratings equal to the maximum for their city.
SELECT cnum, cname, city, rating
FROM cust a
WHERE rating = (SELECT MAX(b.rating) FROM cust b WHERE b.city = a.city);

-- Q61. Find all salespeople who have customers in their cities who they don't service. ( Both way using Join and Correlated subquery.)
-- (a) Using JOIN
SELECT DISTINCT s.snum, s.sname, s.city
FROM salespeople s
JOIN cust c ON s.city = c.city
WHERE c.snum <> s.snum;

-- (b) Using a correlated subquery
SELECT snum, sname, city
FROM salespeople s
WHERE s.city IN (SELECT c.city FROM cust c WHERE c.snum <> s.snum);

-- Q62. Extract cnum,cname and city from customer table if and only if one or more of the customers in the table are located in San Jose.
SELECT cnum, cname, city
FROM cust
WHERE EXISTS (SELECT 1 FROM cust WHERE city = 'San Jose');

-- Q63. Find salespeople no. who have multiple customers.
SELECT snum
FROM cust
GROUP BY snum
HAVING COUNT(*) > 1;

-- Q64. Find salespeople number, name and city who have multiple customers.
SELECT s.snum, s.sname, s.city
FROM salespeople s
WHERE s.snum IN (SELECT snum FROM cust GROUP BY snum HAVING COUNT(*) > 1);

-- Q65. Find salespeople who serve only one customer.
SELECT s.snum, s.sname, s.city
FROM salespeople s
WHERE s.snum IN (SELECT snum FROM cust GROUP BY snum HAVING COUNT(*) = 1);

-- Q66. Extract rows of all salespeople with more than one current order.
SELECT *
FROM salespeople
WHERE snum IN (SELECT snum FROM orders GROUP BY snum HAVING COUNT(*) > 1);

-- Q67. Find all salespeople who have customers with a rating of 300. (use EXISTS)
SELECT *
FROM salespeople s
WHERE EXISTS (SELECT 1 FROM cust c
              WHERE c.snum = s.snum AND c.rating = 300);

-- Q68. Find all salespeople who have customers with a rating of 300. (use Join).
SELECT DISTINCT s.*
FROM salespeople s
JOIN cust c ON s.snum = c.snum
WHERE c.rating = 300;

-- Q69. Select all salespeople with customers located in their cities who are not assigned to them. (use EXISTS).
SELECT *
FROM salespeople s
WHERE EXISTS (SELECT 1 FROM cust c
              WHERE c.city = s.city AND c.snum <> s.snum);

-- Q70. Extract from customers table every customer assigned the a salesperson who currently has at least one other customer ( besides the customer being selected) with orders in order table.
SELECT *
FROM cust a
WHERE EXISTS (SELECT 1
              FROM cust b
              JOIN orders o ON b.cnum = o.cnum
              WHERE b.snum = a.snum AND b.cnum <> a.cnum);

-- Q71. Find salespeople with customers located in their cities ( using both ANY and IN).
-- (a) Using ANY
SELECT *
FROM salespeople
WHERE city = ANY (SELECT city FROM cust);

-- (b) Using IN
SELECT *
FROM salespeople
WHERE city IN (SELECT city FROM cust);

-- Q72. Find all salespeople for whom there are customers that follow them in alphabetical order. (Using ANY and EXISTS)
-- (a) Using ANY
SELECT *
FROM salespeople
WHERE sname < ANY (SELECT cname FROM cust);

-- (b) Using EXISTS
SELECT *
FROM salespeople s
WHERE EXISTS (SELECT 1 FROM cust c WHERE c.cname > s.sname);

-- Q73. Select customers who have a greater rating than any customer in rome.
SELECT *
FROM cust
WHERE rating > ANY (SELECT rating FROM cust WHERE city = 'Rome');

-- Q74. Select all orders that had amounts that were greater that atleast one of the orders from Oct 6th.
SELECT *
FROM orders
WHERE amt > ANY (SELECT amt FROM orders WHERE odate = '1994-10-06');

-- Q75. Find all orders with amounts smaller than any amount for a customer in San Jose. (Both using ANY and without ANY)
-- (a) Using ANY
SELECT *
FROM orders
WHERE amt < ANY (SELECT o.amt FROM orders o
                 JOIN cust c ON o.cnum = c.cnum
                 WHERE c.city = 'San Jose');

-- (b) Without ANY: "smaller than any" = smaller than the biggest one
SELECT *
FROM orders
WHERE amt < (SELECT MAX(o.amt) FROM orders o
             JOIN cust c ON o.cnum = c.cnum
             WHERE c.city = 'San Jose');

-- Q76. Select those customers whose ratings are higher than every customer in Paris. ( Using both ALL and NOT EXISTS).
-- There are no customers in Paris, so the subquery is empty.
-- "> ALL (empty list)" is TRUE, so every customer is returned.
-- (a) Using ALL
SELECT *
FROM cust
WHERE rating > ALL (SELECT rating FROM cust WHERE city = 'Paris');

-- (b) Using NOT EXISTS
SELECT *
FROM cust a
WHERE NOT EXISTS (SELECT 1 FROM cust b
                  WHERE b.city = 'Paris' AND b.rating >= a.rating);

-- Q77. Select all customers whose ratings are equal to or greater than ANY of the Seeres.
SELECT *
FROM cust
WHERE rating >= ANY (SELECT c.rating FROM cust c
                     JOIN salespeople s ON c.snum = s.snum
                     WHERE s.sname = 'Serres');

-- Q78. Find all salespeople who have no customers located in their city. ( Both using ANY and ALL)
-- (a) Using ANY
SELECT *
FROM salespeople
WHERE NOT (city = ANY (SELECT city FROM cust));

-- (b) Using ALL
SELECT *
FROM salespeople
WHERE city <> ALL (SELECT city FROM cust);

-- Q79. Find all orders for amounts greater than any for the customers in London.
SELECT *
FROM orders
WHERE amt > ANY (SELECT o.amt FROM orders o
                 JOIN cust c ON o.cnum = c.cnum
                 WHERE c.city = 'London');

-- Q80. Find all salespeople and customers located in london.
SELECT 'Salesperson' AS type, snum AS num, sname AS name, city
FROM salespeople
WHERE city = 'London'
UNION ALL
SELECT 'Customer', cnum, cname, city
FROM cust
WHERE city = 'London';

-- Q81. For every salesperson, dates on which highest and lowest orders were brought.
SELECT a.snum, a.odate, a.amt, 'Highest' AS order_type
FROM orders a
WHERE a.amt = (SELECT MAX(b.amt) FROM orders b WHERE b.snum = a.snum)
UNION ALL
SELECT a.snum, a.odate, a.amt, 'Lowest'
FROM orders a
WHERE a.amt = (SELECT MIN(b.amt) FROM orders b WHERE b.snum = a.snum)
ORDER BY snum, order_type;

-- Q82. List all of the salespeople and indicate those who don't have customers in their cities as well as those who do have.
SELECT s.snum, s.sname, s.city,
       CASE WHEN EXISTS (SELECT 1 FROM cust c WHERE c.city = s.city)
            THEN 'Has customers in city'
            ELSE 'No customers in city'
       END AS status
FROM salespeople s;

-- Q83. Append strings to the selected fields, indicating weather or not a given salesperson was matched to a customer in his city.
SELECT snum, sname, city, 'MATCHED' AS status
FROM salespeople
WHERE city IN (SELECT city FROM cust)
UNION
SELECT snum, sname, city, 'NO MATCH'
FROM salespeople
WHERE city NOT IN (SELECT city FROM cust WHERE city IS NOT NULL)
ORDER BY snum;

-- Q84. Create a union of two queries that shows the names, cities and ratings of all customers. Those with a rating of 200 or greater will also have the words ‘High Rating', while the others will have the words ‘Low Rating'.
SELECT cname, city, rating, 'High Rating' AS remark
FROM cust
WHERE rating >= 200
UNION
SELECT cname, city, rating, 'Low Rating'
FROM cust
WHERE rating < 200;

-- Q85. Write command that produces the name and number of each salesperson and each customer with more than one current order. Put the result in alphabetical order.
SELECT snum AS num, sname AS name
FROM salespeople s
WHERE (SELECT COUNT(*) FROM orders o WHERE o.snum = s.snum) > 1
UNION
SELECT cnum, cname
FROM cust c
WHERE (SELECT COUNT(*) FROM orders o WHERE o.cnum = c.cnum) > 1
ORDER BY name;

-- Q86. Form a union of three queries. Have the first select the snums of all salespeople in San Jose, then second the cnums of all customers in San Jose and the third the onums of all orders on Oct. 3. Retain duplicates between the last two queries, but eliminates and redundancies between either of them and the first.
-- UNION removes duplicates, UNION ALL keeps them.
SELECT snum AS num FROM salespeople WHERE city = 'San Jose'
UNION
SELECT num FROM (
    SELECT cnum AS num FROM cust   WHERE city = 'San Jose'
    UNION ALL
    SELECT onum        FROM orders WHERE odate = '1994-10-03'
) AS t;

-- Q87. Produce all the salesperson in London who had at least one customer there.
SELECT *
FROM salespeople s
WHERE s.city = 'London'
  AND EXISTS (SELECT 1 FROM cust c
              WHERE c.snum = s.snum AND c.city = 'London');

-- Q88. Produce all the salesperson in London who did not have customers there.
SELECT *
FROM salespeople s
WHERE s.city = 'London'
  AND NOT EXISTS (SELECT 1 FROM cust c
                  WHERE c.snum = s.snum AND c.city = 'London');

-- Q89. We want to see salespeople matched to their customers without excluding those salesperson who were not currently assigned to any customers. (User OUTER join and UNION)
-- (a) Using LEFT OUTER JOIN
SELECT s.snum, s.sname, c.cname
FROM salespeople s
LEFT JOIN cust c ON s.snum = c.snum
ORDER BY s.snum;

-- (b) Using UNION
SELECT s.snum, s.sname, c.cname
FROM salespeople s
JOIN cust c ON s.snum = c.snum
UNION
SELECT snum, sname, 'No customer'
FROM salespeople
WHERE snum NOT IN (SELECT snum FROM cust)
ORDER BY snum;
