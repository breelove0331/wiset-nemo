import sqlite3
import json
import os

def export_to_json():
    db_path = 'data/nemo_data.db'
    json_path = 'data/nemo_data.json'
    
    if not os.path.exists(db_path):
        print(f"Error: {db_path} not found.")
        return

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Select relevant columns
    query = """
    SELECT 
        id, 
        nearSubwayStation, 
        deposit, 
        monthlyRent, 
        size, 
        businessLargeCodeName, 
        businessMiddleCodeName, 
        viewCount, 
        floor
    FROM stores
    """
    
    cursor.execute(query)
    rows = [dict(row) for row in cursor.fetchall()]
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    
    conn.close()
    print(f"Data exported to {json_path}")

if __name__ == "__main__":
    export_to_json()
