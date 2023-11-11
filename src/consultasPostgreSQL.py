import psycopg2
import pandas as pd
from datetime import datetime


def mostrar_datos():
    conn = psycopg2.connect(
        dbname="videojuegos",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    query = pd.read_sql_query("select * from plataformas", conn)

    df = pd.DataFrame(query)
    df.to_csv(datetime.now().strftime("%Y-%m-%d_%I-%M-%S-%p") +
              'plataformas.csv', index=False)
    conn.close()


mostrar_datos()
