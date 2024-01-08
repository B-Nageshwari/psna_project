import subprocess
import json
from datetime import datetime
import psutil
import csv
import speedtest
import time

def collect_metrics():
    # Collect CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)

    # Collect memory usage
    memory_usage = psutil.virtual_memory()

    # Run speedtest-cli and parse its output
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1024 / 1024  # Convert to Mbps
        upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
    except Exception as e:
        print("Speedtest CLI Error:", e)
        download_speed = upload_speed = 0

    # Collect disk I/O stats
    disk_io = psutil.disk_io_counters()

    # Convert bytes to gigabytes for readability
    disk_read_gb = disk_io.read_bytes / (1024 ** 3)
    disk_write_gb = disk_io.write_bytes / (1024 ** 3)

    return {
        "Timestamp": datetime.now(),
        "CPU Usage (%)": cpu_percent,
        "Memory Usage (%)": memory_usage.percent,
        "Download Speed (Mbps)": download_speed,
        "Upload Speed (Mbps)": upload_speed,
        "Disk Read (GB)": disk_read_gb,
        "Disk Write (GB)": disk_write_gb
    }

def save_metrics_to_csv(metrics, csv_filename):
    fieldnames = metrics.keys()

    try:
        with open(csv_filename, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()  # Write header if file is empty
            writer.writerow(metrics)
        print("Metrics saved to", csv_filename)
    except Exception as e:
        print("Error:", e)

def main():
    csv_filename = "metrics_dataset.csv"

    while True:
        metrics = collect_metrics()
        save_metrics_to_csv(metrics, csv_filename)
        time.sleep(10)  #change this if you want to increase the time in seconds.

if __name__ == "__main__":
    main()
