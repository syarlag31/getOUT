import pymysql.cursors
from textmessage import message

current_choice_dict = {
    '0': 'Default/New',
    '1': 'Dining Hall',
    '2': 'Gym',
    '3': 'Groceries',
    '4': 'Movies'
}

connection = pymysql.connect(host='users-database.cds335zym2dr.us-east-1.rds.amazonaws.com',
                             user='admin',
                             password='12345678',
                             database='all_users',
                             cursorclass=pymysql.cursors.DictCursor)

def set_lockout(id: int, set: bool):
    connection.ping()
    with connection:
        with connection.cursor() as cursor:
            sql = f'UPDATE `users` SET `lockout` = {set} WHERE identity = {id}'
            cursor.execute(sql)
        connection.commit()

def get_lockout(id: int) -> bool:
    connection.ping()
    with connection:
        # Check for current choice
        with connection.cursor() as cursor:
            # Get the current choice
            sql = f"SELECT `lockout` FROM `users` WHERE identity = {id}"
            cursor.execute(sql)
            result = cursor.fetchone()
            return (bool(result['lockout']))

def set_choice(id: int, input: int):
    connection.ping()
    with connection:
        with connection.cursor() as cursor:
            sql = f'UPDATE `users` SET `current_choice` = {input} WHERE identity = {id}'
            cursor.execute(sql)
        connection.commit()


def get_email(id: int) -> str:
    connection.ping()
    with connection:
        with connection.cursor() as cursor:
            sql = f"SELECT `email` FROM `users` WHERE identity = {id}"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['email']

def get_name(id: int) -> str:
    connection.ping()
    with connection:
        with connection.cursor() as cursor:
            sql = f"SELECT `full_name` FROM `users` WHERE identity = {id}"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['full_name']

def get_number(id: int) -> str:
    connection.ping()
    with connection:
        with connection.cursor() as cursor:
            sql = f"SELECT `phone_number` FROM `users` WHERE identity = {id}"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['phone_number']

#Formatted like: ('syarlag1@uncc.edu', 'Pass', '7045649676', 'Sathwik Yarlagadda', '0')
def input_user_info(st1, st2, st3, st4, st5):
    connection.ping()
    with connection:
    # Creates a new user
        with connection.cursor() as cursor:
            # Create a new record for users
            sql = "INSERT INTO `users` (`email`, `password`, `phone_number`, `full_name`, `current_choice`) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (st1, st2, st3, st4, st5))
        connection.commit()

# Make sure to attribute user_input with actual userinput
def check_info(email: str, password: str) -> bool:
    connection.ping()
    with connection:
        # Checks for username and password
        with connection.cursor() as cursor:
            # Get the records
            try:
                sql = f"SELECT `email`, `password` FROM `users` WHERE `email` = '{email}' AND `password` = '{password}'"
                cursor.execute(sql)
                result = cursor.fetchone()
                return True
            except:
                return 0

gimme = 0
def set_id(email: str, password: str):
    connection.ping()
    with connection:
        with connection.cursor() as cursor:
            sql = f"SELECT `identity` FROM `users` WHERE `password` = '{password}' AND `email` = '{email}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            global gimme
            gimme = (result['identity'])

def get_id():
    return gimme

def check_email(email: str):
    connection.ping()
    with connection:
        with connection.cursor() as cursor:
            sql = f"SELECT `email`, COUNT(*) FROM `users` GROUP BY `email` HAVING email = '{email}'"
            cursor.execute(sql)
            try:
                result = cursor.fetchone()
                return result['COUNT(*)']
            except:
                return 0

def get_match(id: int, choice: int):
    connection.ping()
    with connection:
        with connection.cursor() as cursor:
            sql = f"SELECT `identity` FROM `users` WHERE `identity` != {id} AND `current_choice` = {choice}" 
            cursor.execute(sql)
            try: 
                result = cursor.fetchone()
                result['identity']
                return True
            except:
                return False

def get_match_id(id: int, choice: int):
    connection.ping()
    with connection:
        with connection.cursor() as cursor:
            sql = f"SELECT `identity` FROM `users` WHERE `identity` != {id} AND `current_choice` = {choice}" 
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['identity']

def set_match(id1, id2):
    connection.ping()
    with connection:
        with connection.cursor() as cursor:
            sql = "UPDATE `users` SET `current_choice` = 0, `lockout` = TRUE WHERE `identity` = %s OR `identity` = %s"
            cursor.execute(sql, (id1, id2))
        connection.commit()
    
    p1_num = get_number(id1)
    p1_name = get_name(id1)
    p2_num = get_number(id2)
    p2_name = get_name(id2)
    message(p1_num, p2_num, p2_name)
    message(p2_num, p1_num, p1_name)