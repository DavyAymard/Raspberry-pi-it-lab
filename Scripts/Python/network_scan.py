#!/usr/bin/env python3
"""
Petit scan réseau basique (ping sur la plage 192.168.1.0/24)
"""

import os

print("🌍 Scan réseau 192.168.1.0/24 en cours...")
for i in range(1, 20):  # Limité à 20 IP pour l'exemple
    ip = f"192.168.1.{i}"
    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
    if response == 0:
        print(f"✅ {ip} est actif")
    else:
        print(f"❌ {ip} ne répond pas")