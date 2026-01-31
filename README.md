# 🔍 File Integrity Checking System (Python)

A Python-based File Integrity Monitoring (FIM) system that detects unauthorized file modifications using cryptographic hashing. The system creates a trusted baseline of files and verifies integrity to identify tampering, deletion, or unauthorized changes. All events are logged into a lightweight SQLite database for auditing and forensic analysis.

---

## 📌 Overview

File Integrity Monitoring is a core cybersecurity mechanism used to detect:
- Malware activity
- Unauthorized configuration changes
- Insider threats
- File tampering on critical systems

This project demonstrates a practical implementation of FIM using Python and cryptographic hash functions.

---

## 🐦‍🔥 Features

- SHA-256 / MD5 based file integrity verification  
- Automated baseline creation  
- Detection of unauthorized file modifications and deletions  
- Recursive directory monitoring  
- SQLite-based logging and auditing  
- Lightweight and scalable design  

---

## 🕹️ Project Structure

file-integrity-monitor/
│
├── baseline.py # Creates trusted file baseline
├── monitor.py # Detects file integrity violations
├── config.json # Configuration file
├── fim.db # SQLite database (auto-generated)
├── requirements.txt
└── README.md


---

## ⚙️ Configuration

Edit `config.json` to define the hashing algorithm and directories to monitor:

```json
{
  "hash_algorithm": "sha256",
  "monitor_paths": [
    "./test_directory"
  ]
}
🐍 Requirements
Python 3.x

No external libraries required (uses built-in modules)

Check Python version:

python --version

🛠️ How to Run
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/file-integrity-monitor.git
cd file-integrity-monitor
2️⃣ Create a Test Directory
mkdir test_directory
echo "test file" > test_directory/test.txt
3️⃣ Create Baseline
python baseline.py
This generates cryptographic hashes and stores them in the database as a trusted baseline.

4️⃣ Modify a File (Simulate Attack)
echo "unauthorized change" >> test_directory/test.txt
5️⃣ Run Integrity Check
python monitor.py
Example output:

🚨 Modified: ./test_directory/test.txt
🗃️ Database Details (fim.db)
The system uses SQLite for logging and auditing.

Tables
baseline
Stores trusted file hashes.

file_path

hash

alerts
Stores detected integrity violations.

file_path

old_hash

new_hash

timestamp

🧠 How It Works:

The system scans configured directories

Cryptographic hashes are generated for each file

A trusted baseline is stored in SQLite

Files are re-scanned during monitoring

Hash mismatches trigger alerts and are logged
