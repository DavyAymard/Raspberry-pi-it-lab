#!/usr/bin/env python3
"""
Affiche des informations système basiques du Raspberry Pi
"""

import platform
import os

print("🔎 Informations Raspberry Pi")
print(f"Système   : {platform.system()}")
print(f"Version   : {platform.version()}")
print(f"Machine   : {platform.machine()}")
print(f"Processeur: {platform.processor()}")
print(f"Noyau     : {platform.release()}")
print(f"Hostname  : {os.uname().nodename}")