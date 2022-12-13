import os
import sqlite3
from sqlalchemy import create_engine


class BD:

    global dir_db_file
    db_file = 'db.sqlite3'
    dir_db_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), db_file)


    def __conn(self):

        conn = sqlite3.connect(dir_db_file)

        return conn


    def execute_sql(self, sql):

        try:

            conn = self.__conn()
            cursor = conn.cursor()
            cursor.execute(sql)

            conn.commit()

        except sqlite3.Error as e:
            print(e)

        finally:
            conn.close()


    def inserir_dados(self, data_frame, table):

        engine = create_engine(f"sqlite:///{dir_db_file}", echo=False)

        try:
            with engine.begin() as conn:
                data_frame.to_sql(table, con=conn, if_exists='replace', chunksize = 1000, index=True)
                return ">>> Dados Inseridos com Sucesso!"

        except Exception as e:
            return f">>> Erro Ao Inserir os Dados!:\n{e}"


    def create_data_table(self, table):

        if table == 'core_odds_prob_ev':
            sql = f"""
                    CREATE TABLE {table} (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL
                    );
                   """

        self.execute_sql(sql)
