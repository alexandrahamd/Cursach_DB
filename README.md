-скрипт для добавления данных в таблицу suppliers

CREATE TABLE suppliers(
id_suppliers int,
company_name,
contact varchar (255),
phone varchar (255),
fax varchar (255),
homepage varchar (255),
country varchar (255),
address varchar (255),
PRIMARY KEY (id_suppliers)
)

main.py

-FOREIGN KEY добавила с помощью execute

-заполнила таблицу suppliers данными из файла JSON с помощью execute

-зменить данные в таблице 'products' столбце 'id_suppliers' 
было NULL стало  id_suppliers 

module_bd.py

-в файле поиск по id в категориях и продуктах.


-