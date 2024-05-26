import sqlite3 as sql

class DataBase:

    def connect(self) -> None:
        self.conn = sql.connect('CadastroClientes.bd')
        self.cursor = self.conn.cursor()
    
    def disconnect(self) -> None:
        self.conn.close()
    
    def monta_tabela(self):
        self.connect()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cadastroclientes
                                (
                                    cod INTEGER PRIMARY KEY,
                                    nome_cliente CHAR(40) NOT NULL,
                                    telefone INTEGER(20),
                                    nascimento CHAR(20),
                                    endereco CHAR(40),
                                    ult_op CHAR(20),
                                    banco CHAR(25),
                                    agencia CHAR(25),
                                    conta CHAR(20),
                                    rg_cnh CHAR(25),
                                    cpf CHAR(20)
                                );
                            """)
        self.conn.commit(); print("Banco de dados criado")
        self.disconnect()