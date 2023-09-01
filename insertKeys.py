from getpass import getpass
from mysql.connector import connect, Error


def get_keys():
    key_file = open("keys.txt", "r")
    lines = key_file.readlines()

    key_file.close
    
    return lines
def check_key(keys):
    try:
        with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
            print(connection)
            insert_keys_query = """
            SELECT *
            FROM lic_keys
            WHERE EXISTS
            (SELECT * FROM lic_keys WHERE %s);
            """

            with connection.cursor() as cursor:
                cursor.execute(insert_keys_query,(keys,))
                result = cursor.fetchall()
                if result == None:
                    return False
                else:
                    return True
                connection.commit()
    except Error as e:
        print(e)


def sort_keys(keys):
    new_keyList = []
    for i in keys:
        isAvKey = check_key(i)
        if isAvKey == False:
            new_keyList.append(i)
    return new_keyList




try:
    with connect(host="localhost",user="kasperky_tg_bot",password='D4tas27w@',database="kaspersky_bot_db") as connection:
        print(connection)
        insert_keys_query = """
        INSERT INTO lic_keys
        (lic_key)
        VALUES ( %s)
        """
        keys = get_keys()
        sort_key_list = keys
        print(keys)
        print(sort_key_list)
        with connection.cursor() as cursor:
            cursor.executemany(insert_keys_query,
                           [(k,) for k in sort_key_list])
            connection.commit()
except Error as e:
    print(e)
