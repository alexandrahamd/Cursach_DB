
--Страница «Товары» (products_page)
--Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood,
--которых в продаже менее 20 единиц. Вывести наименование продуктов, кол-во единиц в продаже, 
--имя контакта поставщика и его телефонный номер.

SELECT product_name, units_in_stock, suppliers.contact, suppliers.phone FROM products
JOIN categories USING (category_id)
JOIN suppliers USING (id_suppliers)
WHERE categories.category_name IN ('Beverages','Seafood')
AND units_in_stock >= 20



