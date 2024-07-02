import os
import shutil
import time
import hashlib
import argparse
from datetime import datetime

def calculate_md5(file_path):
    #Calculate the MD5 checksum of a file.
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def log(message, log_file):
    #Log a message to the console and a log file.
    print(message)
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

def sync_folders(source, replica, log_file):
    #Synchronize the replica folder with the source folder.
    source_files = {}
    for root, _, files in os.walk(source):
        for file in files:
            source_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_file_path, source)
            source_files[relative_path] = source_file_path

    replica_files = {}
    for root, _, files in os.walk(replica):
        for file in files:
            replica_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(replica_file_path, replica)
            replica_files[relative_path] = replica_file_path

    # Copy new and modified files from source to replica
    for relative_path, source_file_path in source_files.items():
        replica_file_path = os.path.join(replica, relative_path)
        if (relative_path not in replica_files or 
            calculate_md5(source_file_path) != calculate_md5(replica_file_path)):
            os.makedirs(os.path.dirname(replica_file_path), exist_ok=True)
            shutil.copy2(source_file_path, replica_file_path)
            log(f"Copied/Updated: {relative_path}", log_file)

    # Remove files from replica that are not in source
    for relative_path in replica_files:
        if relative_path not in source_files:
            os.remove(replica_files[relative_path])
            log(f"Removed: {relative_path}", log_file)

def main():
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument("source", type=str, help="Path to the source folder")
    parser.add_argument("replica", type=str, help="Path to the replica folder")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("log_file", type=str, help="Path to the log file")

    args = parser.parse_args()

    # Ensure the log file directory exists
    os.makedirs(os.path.dirname(args.log_file), exist_ok=True)

    while True:
        sync_folders(args.source, args.replica, args.log_file)
        time.sleep(args.interval)

if __name__ == "__main__":
    main()