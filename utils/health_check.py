import psutil
from utils.webex_alert import send_webex_alert
from datetime import datetime

def check_system(cpu_threshold, memory_threshold, disk_threshold, bot_token, room_id):
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent / (1024 * 1024)  # in MB
    bytes_recv = net_io.bytes_recv / (1024 * 1024)  # in MB

    log_message = (
        f"System Health Report:\n"
        f"CPU Usage: {cpu_usage}%\n"
        f"Memory Usage: {memory_usage}%\n"
        f"Disk Usage: {disk_usage}%\n"
        f"Network Sent: {bytes_sent:.2f} MB\n"
        f"Network Received: {bytes_recv:.2f} MB"
    )
    print(log_message)

    # Only alert if thresholds are crossed
    if cpu_usage > cpu_threshold or memory_usage > memory_threshold or disk_usage > disk_threshold:
        alert_message = (
            f"⚠️ ALERT — System Threshold Exceeded:\n"
            f"{log_message}"
        )
        send_webex_alert(bot_token, room_id, alert_message)

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Check executed")
