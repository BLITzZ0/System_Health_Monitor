import time
import schedule
from dotenv import load_dotenv
import os
from utils.health_check import check_system

load_dotenv()

CPU_THRESHOLD = int(os.getenv("CPU_THRESHOLD", 80))
MEMORY_THRESHOLD = int(os.getenv("MEMORY_THRESHOLD", 80))
DISK_THRESHOLD = int(os.getenv("DISK_THRESHOLD", 90))
BOT_TOKEN = os.getenv("BOT_TOKEN")
ROOM_ID = os.getenv("ROOM_ID")

print("🚀 System Health Monitor started...")

schedule.every(10).seconds.do(check_system, CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD, BOT_TOKEN, ROOM_ID)

while True:
    schedule.run_pending()
    time.sleep(1)
