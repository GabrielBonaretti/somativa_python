from modules.conectar import conexao
from modules.conectar import cursor
from modules.Web_Scraping import Web


def ler_lista(nome_loja):
    try:
        sql = f'SELECT * from {nome_loja}'
        cursor.execute(sql)
        lista_usuarios = cursor.fetchall()
        return lista_usuarios
    except:
        lista_usuarios = []
        return lista_usuarios



def deletar_tabela(nome_loja):
    sql = f'DROP TABLE IF EXISTS {nome_loja};'
    cursor.execute(sql)
    conexao.commit()  # edita o banco de dados (create, update, delete)


def criar_tabela(nome_loja):
    sql = f'''CREATE TABLE `celulares`.`{nome_loja}` (
                `idnew_table` INT NOT NULL AUTO_INCREMENT,
                `nome` VARCHAR(255) NULL,
                `modelo` VARCHAR(255) NULL,
                `preco` DOUBLE NULL,
                `loja` VARCHAR(255) NULL,
                PRIMARY KEY (`idnew_table`));'''
    cursor.execute(sql)
    conexao.commit()  # edita o banco de dados (create, update, delete)

    web = Web()
    if nome_loja == "kabum":
        celulares_lista = web.abrir_kabum()
    else:
        celulares_lista = web.abrir_kalunga()

    for i in range(len(celulares_lista)):
        sql = f'INSERT INTO {nome_loja} (nome, modelo, preco, loja) VALUES ("{celulares_lista[i][0]}", "{celulares_lista[i][1]}", {celulares_lista[i][2]}, "{nome_loja}")'
        cursor.execute(sql)
        conexao.commit()  # edita o banco de dados (create, update, delete)
