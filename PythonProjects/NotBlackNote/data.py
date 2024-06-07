import sqlite3 as sql

class Repository:

    def connect(self) -> None:
        self.conn = sql.connect('lista_tarefas.bd')
        self.cursor = self.conn.cursor()

    def disconnect(self) -> None:
        self.conn.close()

    def monta_(self) -> None:
        self.connect()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS lista_tarefas.bd
                (
                    texto CHAR(5000),
                    favorito_cond BOOL,
                    senha_cond BOOL,
                    senha CHAR(4),
                    categoria CHAR(40),
                    data_cri CHAR(20),
                    data_modi CHAR(20),
                    tamanho INTEGER(10),

                );
        """)
        self.conn.commit()
        self.disconnect()
    
