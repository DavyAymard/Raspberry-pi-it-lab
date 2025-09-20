#!/usr/bin/env python3
"""
Mini monitoring CPU & RAM avec psutil.
"""

import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    print(f"⚙️ CPU: {cpu}% | 🧠 RAM: {ram}%")
    time.sleep(2)