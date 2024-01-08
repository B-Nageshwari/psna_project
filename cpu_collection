import psutil
import speedtest
import csv
from datetime import datetime
import time

def collect_metrics():
    # Collect CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)

    # Collect memory usage
    memory_usage = psutil.virtual_memory()

    # Collect network usage
    st = speedtest.Speedtest()
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

    # Collect disk I/O stats
    disk_io = psutil.disk_io_counters()

    return {
        "Timestamp": datetime.now(),
        "CPU Usage (%)": cpu_percent,
        "Memory Usage (%)": memory_usage.percent,
        "Download Speed (Mbps)": download_speed,
        "Upload Speed (Mbps)": upload_speed,
        "Disk Read Bytes": disk_io.read_bytes,
        "Disk Write Bytes": disk_io.write_bytes
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
    csv_filename = "metrics_datasets.csv"

    while True:
        metrics = collect_metrics()
        save_metrics_to_csv(metrics, csv_filename)
        time.sleep(60)  # Sleep for 1 minute (60 seconds)

if __name__ == "__main__":
    main()
