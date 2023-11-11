import mysql.connector
import pandas as pd
from datetime import datetime



def mostrar_datos():
    cnn = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user= 'root',
        password = 'Micontrasena',
        db = 'videojuegos'
    )
    query = pd.read_sql_query("select * from videojuegos", cnn)
    
    df = pd.DataFrame(query)
    df.to_csv(datetime.now().strftime("%Y-%m-%d_%I-%M-%S-%p") +
              'videojuegos.csv', index=False)


mostrar_datos()