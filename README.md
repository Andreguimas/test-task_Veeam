# test-task_Veeam

# Folder Synchronization Script

This Python script synchronizes two folders: 'source' and 'replica', maintaining an identical copy of the 'source' folder at the 'replica' folder. The synchronization is one-way, meaning changes in the 'source' folder are reflected in the 'replica' folder, but not vice versa.

## Features

- One-way synchronization from 'source' to 'replica'
- Periodic synchronization at user-defined intervals (ex:60 sec)
- Logging of file operations (creation, copying, removal) to console and log file

## Requirements

- Python 3.x

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Andreguimas/test-task_Veeam.git
    cd folder-sync-script
    ```

2. **Install required libraries:**

    This script uses only Python's standard libraries, so no additional installation is needed.

## Usage

Run the script using the following command:

```sh
python folder_sync.py <source_folder_path> <replica_folder_path> <interval_in_seconds> <log_file_path>

example:
python folder_sync.py /path/to/source /path/to/replica 60 /path/to/logfile.log

## Arguments

<source_folder_path>: Path to the source folder.
<replica_folder_path>: Path to the replica folder.
<interval_in_seconds>: Time interval between synchronizations (in seconds).
<log_file_path>: Path to the log file.
