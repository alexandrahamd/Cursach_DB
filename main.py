import json
import psycopg2


conn = psycopg2.connect(database='Northwind Traders ',user='postgres', password='12345')
try:
    with conn:
        with conn.cursor() as cur:
            with open('suppliers.json') as f:
                templates = json.load(f)

            #добавить FOREIGN KEY
            cur.execute('ALTER TABLE products ADD FOREIGN KEY (id_suppliers) '
                        'REFERENCES suppliers(id_suppliers)')

            #заполнить таблицу suppliers данными из файла JSON
            for i in range(len(templates)):
                company_name = templates[i].get("company_name")
                contact = templates[i].get("contact")
                phone = templates[i].get("phone")
                fax = templates[i].get("fax")
                homepage = templates[i].get("homepage")
                address_country = templates[i].get('address').split(';')[0]
                address_full = "".join(templates[i].get('address').split(';')[1:])
                cur.execute('INSERT INTO suppliers VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
                            (i+1, company_name, contact, phone, fax, homepage,
                             address_country, address_full))

            #апрос для получение информации из БД
            postgreSQL_select_Query = "SELECT product_id, product_name FROM products"
            cur.execute(postgreSQL_select_Query)
            # Выбор строк из таблицы с помощью cursor.fetchall
            records = cur.fetchall()

            # создать словарь {product_id: product_name}
            products_dic = {}
            for row in records:
                products_dic.update({row[1]: row[0]})

            # создать список продуктов из файла json
            templat_list = []
            i = 1
            for item in templates:
                product_list = item.get('products')
                templat_list.append(product_list)
                i += 1

            #создать словарь {product_id: id_suppliers}
            result_dict = {}
            for item_product in products_dic:
                for item_templ in templat_list:
                    if item_product in item_templ:
                        result_dict.update({products_dic[item_product]: templat_list.index(item_templ)+1})

            #зменить данные в таблице 'products' столбце 'id_suppliers'
            for item in result_dict:
                value_id_suppliers = result_dict[item]
                value_product_id = item
                print(value_id_suppliers, value_product_id)
                cur.execute("""UPDATE products SET id_suppliers=%s WHERE product_id=%s""",
                               (value_id_suppliers, value_product_id))
finally:
    conn.close()
