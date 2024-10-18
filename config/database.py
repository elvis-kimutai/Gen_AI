import psycopg2
from psycopg2 import sql

DATABASE_URL = "postgresql://inventory_db_dbnj_user:XztJiqM6PGprH34UUIAuQIn4GmYGn7ww@dpg-cs7mfqrv2p9s73f5ei5g-a.oregon-postgres.render.com/inventory_db_dbnj"

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id SERIAL PRIMARY KEY,
            item_name VARCHAR(255) NOT NULL,
            category VARCHAR(255),
            quantity INTEGER,
            price DECIMAL(10, 2),
            description TEXT
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()
