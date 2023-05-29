import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='celulares'
)

cursor = conexao.cursor()

if conexao.is_connected():
    print(f'conectou a {conexao.get_server_info()}')