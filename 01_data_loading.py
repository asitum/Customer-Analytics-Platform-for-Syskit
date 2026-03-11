"""
Syskit Customer Analytics - Data Loading Module
Author: Antoni Šitum
"""

import sqlite3
import pandas as pd

def load_data(db_path):
    """Load all tables from SQLite database"""
    conn = sqlite3.connect(db_path)
    
    tables = ['tenants', 'subscriptions', 'events', 'users', 
              'crm_companies', 'crm_activities']
    
    data = {}
    for table in tables:
        try:
            data[table] = pd.read_sql(f"SELECT * FROM {table};", conn)
            print(f"✅ Loaded {table}: {len(data[table])} rows")
        except:
            print(f"❌ Could not load {table}")
    
    conn.close()
    return data

if __name__ == "__main__":
    print("Syskit Data Loading Module")
