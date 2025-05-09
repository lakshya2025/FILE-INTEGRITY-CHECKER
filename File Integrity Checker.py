import hashlib
import os
import json

HASH_RECORD_FILE = "hash_records.json"

def calculate_hash(filepath):
    """Calculate SHA-256 hash of the file"""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def scan_directory(directory):
    """Scan a directory and return a dictionary of file paths and their hashes"""
    hash_data = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            file_hash = calculate_hash(full_path)
            if file_hash:
                hash_data[full_path] = file_hash
    return hash_data

def save_hashes(hash_data):
    with open(HASH_RECORD_FILE, 'w') as f:
        json.dump(hash_data, f, indent=4)

def load_previous_hashes():
    if os.path.exists(HASH_RECORD_FILE):
        with open(HASH_RECORD_FILE, 'r') as f:
            return json.load(f)
    return {}

def check_integrity(current_hashes, old_hashes):
    added = []
    removed = []
    modified = []

    old_files = set(old_hashes.keys())
    current_files = set(current_hashes.keys())

    added = list(current_files - old_files)
    removed = list(old_files - current_files)

    for file in current_files & old_files:
        if current_hashes[file] != old_hashes[file]:
            modified.append(file)

    return added, removed, modified

def main():
    directory = input("Enter the directory to scan: ")
    print("\nScanning directory for file integrity...")

    old_hashes = load_previous_hashes()
    current_hashes = scan_directory(directory)

    added, removed, modified = check_integrity(current_hashes, old_hashes)

    if not (added or removed or modified):
        print("✅ No changes detected. All files are intact.")
    else:
        print("⚠️ Changes detected:")
        if added:
            print("\n➕ Added files:")
            for f in added:
                print("  -", f)
        if removed:
            print("\n➖ Removed files:")
            for f in removed:
                print("  -", f)
        if modified:
            print("\n✏️ Modified files:")
            for f in modified:
                print("  -", f)

    save_hashes(current_hashes)

if __name__ == "__main__":
    main()
