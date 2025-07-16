import sqlite3
import requests
import uuid
import datetime
import json
import time
import math
from datetime import timezone

DB_PATH = input("Enter path to x-ui.db: ").strip()
API_URL = input("Enter full Hiddify API endpoint (e.g., https://domain.com/proxy/api/v2/admin/user/): ").strip()
API_KEY = input("Enter your Hiddify API Key: ").strip()
DELAY = 0.5  # seconds between requests

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Hiddify-API-Key": API_KEY
}

def ms_to_days(expiry_ms):
    now_ms = int(datetime.datetime.now(timezone.utc).timestamp() * 1000)
    remaining_ms = expiry_ms - now_ms
    if remaining_ms <= 0:
        return 0
    days = remaining_ms / (24 * 60 * 60 * 1000)
    return math.ceil(days)

def bytes_to_gb(bytes_val):
    return round(bytes_val / (1024 ** 3), 3)

def migrate_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT email, up, down, total, expiry_time FROM client_traffics")
    users = cursor.fetchall()

    results = []

    for email, up, down, total, expiry_time in users:
        usage = bytes_to_gb((up or 0) + (down or 0))
        limit = bytes_to_gb(total or 0)
        package_days = ms_to_days(expiry_time) if expiry_time else 0
        username = (email or str(uuid.uuid4())[:8]).split("@")[0]

        payload = {
            "added_by_uuid": API_KEY,
            "comment": None,
            "current_usage_GB": usage,
            "ed25519_private_key": "string",
            "ed25519_public_key": "string",
            "enable": True,
            "is_active": True,
            "lang": "fa",
            "last_online": None,
            "last_reset_time": None,
            "mode": "no_reset",
            "name": username,
            "package_days": package_days,
            "start_date": None,
            "telegram_id": 0,
            "usage_limit_GB": limit,
            "uuid": None,
            "wg_pk": "string",
            "wg_psk": "string",
            "wg_pub": "string"
        }

        try:
            res = requests.post(API_URL, headers=HEADERS, json=payload, timeout=15)
            success = res.status_code == 200 or res.status_code == 201
            result = {
                "name": username,
                "status_code": res.status_code,
                "response": res.text,
                "success": success
            }
            print(f"[{'✓' if success else '✗'}] {username} → {res.status_code}")
        except Exception as e:
            result = {
                "name": username,
                "error": str(e),
                "success": False
            }
            print(f"[✗] {username} → Error: {str(e)}")

        results.append(result)
        time.sleep(DELAY)

    with open("migration_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("\nMigration completed. Results saved to migration_results.json")

if __name__ == "__main__":
    migrate_users()
