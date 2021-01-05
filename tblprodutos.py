import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(user='root', password='123456',
                                  host='localhost',
                                  database='db_MeusLivros')

    inserir_produtos = """INSERT INTO tbl_produtos
                            (IdProduto, NomeProduto, Preco, Quantidade)
                          VALUES
                            (1,'Camera',850.00,5),
                            (2,'Monitor',630.00,7),
                            (3,'Relógio',575.00,10),
                            (4,'Camera',850.00,5),
                            (5,'Monitor',630.00,7),
                            (6,'Relógio',575.00,10)
                       """
    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(cursor.rowcount, "registros inseridos na tabela!")
    cursor.close()
except Error as erro:
    print("Falha ao inserir dados no MySQL: {}".format(erro))
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print("Conexao ao MySQL finalizada")