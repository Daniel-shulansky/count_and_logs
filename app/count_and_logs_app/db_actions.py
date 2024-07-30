import datetime
import os
import socket
import mysql.connector


# password = os.getenv('DB_PASS')


def establish_connection():
    connection = mysql.connector.connect(user='admin',
                                         password='1234admin',
                                         host='daniel-task-db.coow8klldjgb.us-east-1.rds.amazonaws.com',
                                         database='count_app',
                                         port=3306)

    return connection


def get_count():
    conn = establish_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT count FROM counter;')
    counts = cursor.fetchone()
    count = counts[0]

    conn.close()
    cursor.close()

    return count


def increment_count():
    conn = establish_connection()
    cursor = conn.cursor()

    cursor.execute('UPDATE counter SET count = count + 1;')
    conn.commit()

    cursor.close()
    conn.close()


def access(remote_ip):
    conn = establish_connection()
    cursor = conn.cursor()

    local_ip = socket.gethostbyname(socket.gethostname())
    client_ip = remote_ip
    current_date = datetime.datetime.now()
    current_date.strftime('%Y-%m-%d %H:%M:%S')

    query = 'INSERT INTO access_log (access_time, client_ip, internal_ip) VALUES (%s, %s, %s)'
    values = (current_date, client_ip, local_ip)
    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return local_ip

