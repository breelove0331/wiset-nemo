import requests
import sqlite3
import json
import os
import time

def fetch_nemo_data(page_index=0):
    url = "https://www.nemoapp.kr/api/store/search-list"
    params = {
        "Subway": "222",
        "Radius": "1000",
        "CompletedOnly": "false",
        "NELat": "37.50296615311945",
        "NELng": "127.03781866468543",
        "SWLat": "37.482536912853405",
        "SWLng": "127.01031137257874",
        "Zoom": "15",
        "SortBy": "29",
        "PageIndex": str(page_index)
    }
    
    headers = {
        "referer": "https://www.nemoapp.kr/store",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }

    print(f"Fetching Page {page_index}...")
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error on Page {page_index}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception on Page {page_index}: {e}")
        return None

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            if v and all(isinstance(i, (str, int, float)) for i in v):
                items.append((new_key, '|'.join(map(str, v))))
            else:
                items.append((new_key, json.dumps(v, ensure_ascii=False)))
        else:
            items.append((new_key, v))
    return dict(items)

def save_to_sqlite(items, is_first_page=False):
    if not items:
        return

    # 데이터 평탄화 적용
    flattened_items = [flatten_dict(item) for item in items]

    db_path = os.path.join('data', 'nemo_data.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if is_first_page:
        # 첫 페이지일 경우에만 기존 테이블 삭제 및 재생성
        cursor.execute("DROP TABLE IF EXISTS stores")
        
        sample_item = flattened_items[0]
        columns = []
        for key, value in sample_item.items():
            if isinstance(value, int):
                columns.append(f"[{key}] INTEGER")
            elif isinstance(value, float):
                columns.append(f"[{key}] REAL")
            else:
                columns.append(f"[{key}] TEXT")
        
        create_table_query = f"CREATE TABLE IF NOT EXISTS stores ({', '.join(columns)})"
        cursor.execute(create_table_query)

    # 데이터 삽입
    # 컬럼 정보를 다시 가져와서 안전하게 삽입
    cursor.execute("PRAGMA table_info(stores)")
    table_cols = [col[1] for col in cursor.fetchall()]
    
    placeholders = ', '.join(['?' for _ in table_cols])
    insert_query = f"INSERT INTO stores ({', '.join([f'[{k}]' for k in table_cols])}) VALUES ({placeholders})"

    for item in flattened_items:
        # 테이블 컬럼 순서에 맞춰 값 리스트 생성
        values = [item.get(key) for key in table_cols]
        cursor.execute(insert_query, values)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    page = 0
    total_count = 0
    
    while True:
        data = fetch_nemo_data(page)
        
        if not data or 'items' not in data or not data['items']:
            print(f"No more data found at Page {page}. Stopping.")
            break
            
        items = data['items']
        save_to_sqlite(items, is_first_page=(page == 0))
        
        count = len(items)
        total_count += count
        print(f"Saved {count} items from Page {page}. (Total: {total_count})")
        
        page += 1
        time.sleep(1)  # 서버 부하 방지를 위한 지연

    print(f"Finished! Total items collected: {total_count}")
