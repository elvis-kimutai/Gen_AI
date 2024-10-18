from config.database import get_db_connection

def get_all_items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return items

def add_item(item_name, category, quantity, price, description):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO inventory (item_name, category, quantity, price, description) VALUES (%s, %s, %s, %s, %s)",
                (item_name, category, quantity, price, description))
    conn.commit()
    cur.close()
    conn.close()

def update_item(id, item_name, category, quantity, price):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE inventory SET item_name=%s, category=%s, quantity=%s, price=%s WHERE id=%s",
                (item_name, category, quantity, price, id))
    conn.commit()
    cur.close()
    conn.close()

def delete_item(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM inventory WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
