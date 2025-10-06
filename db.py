import os
import pymysql

DB_HOST = os.getenv("ROAD_DB_HOST")
DB_USER = os.getenv("ROAD_DB_USER")
DB_PASSWORD = os.getenv("ROAD_DB_PASSWORD")
DB_NAME = os.getenv("ROAD_DB_NAME")
DB_PORT = int(os.getenv("ROAD_DB_PORT"))

def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        port=DB_PORT
    )

def create_users_table():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(20) PRIMARY KEY,
                created_at DATETIME NOT NULL,
                status ENUM('active', 'finish') DEFAULT 'active'
            );
            """)
        conn.commit()
    finally:
        conn.close()