#!/usr/bin/env python3
"""
Logger simple pour capteur GPIO (ex: bouton ou capteur de mouvement).
"""

import RPi.GPIO as GPIO
import time

PIN = 17  # Exemple : broche GPIO 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

print("🔎 Surveillance du capteur... (CTRL+C pour arrêter)")
try:
    while True:
        if GPIO.input(PIN):
            print("⚡ Signal détecté !")
        time.sleep(1)
except KeyboardInterrupt:
    print("Arrêt du programme")
finally:
    GPIO.cleanup()