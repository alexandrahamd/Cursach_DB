import psycopg2
import json


def get_product_by_id(config, id):
    conn = psycopg2.connect(database=config.get('database'), user=config.get('user'), password=config.get('password'))
    try:
        with conn:
            with conn.cursor() as cur:

                # запрос с БД
                cur.execute('SELECT product_id, product_name, categories.category_name, unit_price '
                            'FROM products JOIN categories USING(category_id) WHERE product_id =(%s)', (id, ))
                records = cur.fetchall()

                # запись данных из БД в словарь
                records_dict = {'product_id': records[0][0], 'product_name': records[0][1],
                                'category_name': records[0][2],'unit_price':records[0][3]}

                # преоброзование в JSON формат
                jsonstr = json.dumps(records_dict)
                return jsonstr
    finally:
        conn.close()


def get_category_by_id(config, id):
    conn = psycopg2.connect(database=config.get('database'), user=config.get('user'), password=config.get('password'))
    try:
        with conn:
            with conn.cursor() as cur:
                # запрос с БД
                cur.execute('SELECT category_id, category_name, description, products.product_name '
                            'from categories JOIN products USING(category_id)WHERE category_id =(%s)', (id,))
                records = cur.fetchall()

                list_product = []
                for i in range(len(records)):
                    list_product.append(records[i][3])

                # запись данных из БД в словарь
                records_dict = {'category_id': records[0][0], 'category_name': records[0][1],
                                'description': records[0][2], 'product_names': list_product}

                # преоброзование в JSON формат
                jsonstr = json.dumps(records_dict)
                return jsonstr
    finally:
        conn.close()


if __name__ == '__main__':
    config = {'database': 'Northwind Traders ','user': 'postgres', 'password': '12345'}
    print(get_product_by_id(config, 4))
    print(get_category_by_id(config, 4))
