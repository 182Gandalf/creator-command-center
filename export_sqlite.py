#!/usr/bin/env python3
"""
SQLite to PostgreSQL Migration Script for FlowCast

This script exports all data from the SQLite database to JSON format,
which can then be imported into PostgreSQL.
"""

import sqlite3
import json
import os
from datetime import datetime

def export_sqlite_data():
    """Export all data from SQLite to JSON files"""
    print("🔄 Exporting SQLite data...")
    
    db_path = 'instance/creator_command_center.db'
    if not os.path.exists(db_path):
        print(f"❌ Database not found at {db_path}")
        return None
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    data = {
        'users': [],
        'posts': [],
        'content_ideas': [],
        'ai_usage_trackers': [],
        'exported_at': datetime.utcnow().isoformat()
    }
    
    # Get table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    print(f"   Found tables: {', '.join(tables)}")
    
    # Export Users
    if 'users' in tables:
        print("  📦 Exporting users...")
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            data['users'].append(dict(row))
        print(f"      {len(rows)} users exported")
    
    # Export Posts
    if 'posts' in tables:
        print("  📦 Exporting posts...")
        cursor.execute("SELECT * FROM posts")
        rows = cursor.fetchall()
        for row in rows:
            data['posts'].append(dict(row))
        print(f"      {len(rows)} posts exported")
    
    # Export Content Ideas
    if 'content_ideas' in tables:
        print("  📦 Exporting content ideas...")
        cursor.execute("SELECT * FROM content_ideas")
        rows = cursor.fetchall()
        for row in rows:
            data['content_ideas'].append(dict(row))
        print(f"      {len(rows)} content ideas exported")
    
    # Export AI Usage Trackers
    if 'ai_usage_tracker' in tables:
        print("  📦 Exporting AI usage trackers...")
        cursor.execute("SELECT * FROM ai_usage_tracker")
        rows = cursor.fetchall()
        for row in rows:
            data['ai_usage_trackers'].append(dict(row))
        print(f"      {len(rows)} AI usage trackers exported")
    
    conn.close()
    
    # Save to file
    export_file = 'migration_data.json'
    with open(export_file, 'w') as f:
        json.dump(data, f, indent=2, default=str)
    
    print(f"\n✅ Export complete!")
    print(f"📁 Data saved to: {export_file}")
    
    return export_file

if __name__ == '__main__':
    export_sqlite_data()
