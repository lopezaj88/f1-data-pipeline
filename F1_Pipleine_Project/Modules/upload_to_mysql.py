import mysql.connector
import pandas as pd

def upload_to_mysql(csvFile, tableName, mysqlConfig):
    """
    Uploads a CSV file to a MySQL table.
    Args:
        csv_file (str): Path to the CSV file.
        table_name (str): Name of the table in the database.
        mysql_config (dict): MySQL connection details from config.json.
    """
    connection = mysql.connector.connect(
        host=mysqlConfig["host"],
        port=mysqlConfig["port"],  # Include the port number
        user=mysqlConfig["user"],
        password=mysqlConfig["password"],
        database=mysqlConfig["database"]
    )
    cursor = connection.cursor()

    # Load the CSV data
    data = pd.read_csv(csvFile)
    cols = ",".join(data.columns)
    placeholders = ",".join(["%s"] * len(data.columns))
    query = f"INSERT INTO {tableName} ({cols}) VALUES ({placeholders})"

    # Insert rows into the table
    for _, row in data.iterrows():
        cursor.execute(query, tuple(row))

    connection.commit()
    cursor.close()
    connection.close()
    print(f"Data from {csvFile} uploaded to MySQL table {tableName}")
