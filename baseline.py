import hashlib, os, json, sqlite3

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
CREATE TABLE IF NOT EXISTS baseline (
    file_path TEXT PRIMARY KEY,
    hash TEXT
)
""")

for path in config["monitor_paths"]:
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                file_hash = get_hash(full_path, config["hash_algorithm"])
                cursor.execute(
                    "INSERT OR REPLACE INTO baseline VALUES (?,?)",
                    (full_path, file_hash)
                )
            except:
                pass

conn.commit()
conn.close()

print("👌 Baseline created successfully.")
