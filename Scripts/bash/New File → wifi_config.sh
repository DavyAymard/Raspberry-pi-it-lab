#!/bin/bash
# wifi_config.sh - Script de configuration Wi-Fi rapide pour Raspberry Pi IT Lab

SSID=$1
PASSWORD=$2

if [ -z "$SSID" ] || [ -z "$PASSWORD" ]; then
    echo "Usage: $0 <SSID> <PASSWORD>"
    exit 1
fi

echo "network={
    ssid=\"$SSID\"
    psk=\"$PASSWORD\"
}" | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf > /dev/null

sudo wpa_cli -i wlan0 reconfigure
echo "✅ Wi-Fi configuré avec succès pour $SSID"