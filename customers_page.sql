--customers_page
-- Посчитать количество заказчиков
select count(*) from customers

-- Выбрать все уникальные сочетания городов и стран, в которых "зарегестрированы" заказчики

select DISTINCT city from customers,
select DISTINCT country from customers

-- Найти заказчиков и обслуживающих их заказы сотрудников, таких, что и заказчики
--и сотрудники из города London, а доставка идёт компанией Speedy Express. 
--Вывести компанию заказчика и ФИО сотрудника.


SELECT customers.company_name, 
CONCAT(employees.first_name, ' ', employees.last_name)
FROM orders 
JOIN customers USING(customer_id)
JOIN employees USING(employee_id)
JOIN shippers ON orders.ship_via = shippers.shipper_id
WHERE employees.city = 'London' AND customers.city = 'London'
AND shippers.company_name = 'Speedy Express'


-- Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.
SELECT company_name, order_id
FROM orders
FULL JOIN customers USING(customer_id)
WHERE order_id is Null

