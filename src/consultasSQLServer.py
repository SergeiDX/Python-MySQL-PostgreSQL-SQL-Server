import pyodbc as odbc
import pandas as pd
from datetime import datetime

def mostrar_datos():
    cnn = odbc.connect(
        'Driver={SQL Server Native Client 16.0};'
        'Server=DESKTOP-EUB75BK;'
        'Database=Videojuegos;'
        'Trusted_Connection=yes;'
    )
    query = pd.read_sql_query("select * from videojuegos", cnn)
    
    df = pd.DataFrame(query)
    df.to_csv(datetime.now().strftime("%Y-%m-%d_%I-%M-%S-%p") +
              'videojuegos.csv', index=False)


mostrar_datos()