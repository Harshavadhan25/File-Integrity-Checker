import hashlib, os, json, sqlite3, datetime

def get_hash(file_path, algo):
    h = hashlib.new(algo)
    with open(file_path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

with open("config.json") as f:
    config = json.load(f)

conn = sqlite3.connect("fim.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    file_path TEXT,
    old_hash TEXT,
    new_hash TEXT,
    timestamp TEXT
)
""")

cursor.execute("SELECT file_path, hash FROM baseline")
baseline_data = dict(cursor.fetchall())

for file_path, old_hash in baseline_data.items():
    if os.path.exists(file_path):
        try:
            new_hash = get_hash(file_path, config["hash_algorithm"])
            if new_hash != old_hash:
                cursor.execute(
                    "INSERT INTO alerts VALUES (?,?,?,?)",
                    (file_path, old_hash, new_hash, str(datetime.datetime.now()))
                )
                print(f"🚨 Modified: {file_path}")
        except:
            pass
    else:
        print(f"🤷‍♀️ Deleted: {file_path}")

conn.commit()
conn.close()
