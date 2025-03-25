import os

def delete_logs_at_20gb(log_dir):
    """
    Deletes logs in the specified directory when the total size reaches or exceeds 20GB.

    Args:
        log_dir (str): Path to the log directory.
    """
    size_limit_gb = 20.0
    total_size = 0
    log_files = []

    # Calculate total size and collect log files
    for dirpath, dirnames, filenames in os.walk(log_dir):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                file_size = os.path.getsize(fp)
                total_size += file_size
                log_files.append((fp, file_size))

    # Convert total size to GB
    total_size_gb = total_size / (1024 ** 3)

    # If size reaches or exceeds 20GB, delete logs
    if total_size_gb >= size_limit_gb:
        deleted_size = 0
        for log_file, file_size in sorted(log_files, key=lambda x: os.path.getmtime(x[0])):
            try:
                os.remove(log_file)
                deleted_size += file_size
                if (total_size - deleted_size) / (1024 ** 3) < size_limit_gb:
                    break
            except Exception as e:
                print(f"Error deleting file {log_file}: {e}")

        print(f"Deleted logs to bring total size below 20GB")
    else:
        print(f"Current log size: {total_size_gb:.2f}GB. No deletion needed.")

# Example usage
log_dir = "logs"  # Replace with the actual log directory path
delete_logs_at_20gb(log_dir)
