
--Страница «Сотрудники» (employees_page)
--Выбрать записи работников (включить колонки имени, фамилии, телефона, региона)
--в которых регион неизвестен

SELECT last_name, first_name, home_phone ,region FROM employees
WHERE region is NULL


--Выбрать такие страны в которых "зарегистированы" одновременно заказчики и
--поставщики, но при этом в них не "зарегистрированы" работники

SELECT country FROM employees
UNION
SELECT country FROM suppliers
INTERSECT
SELECT country FROM customers
