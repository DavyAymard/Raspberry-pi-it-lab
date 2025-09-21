# Installation et configuration de base du Raspberry Pi IT Lab

## Étapes rapides

1. Téléchargez **Raspberry Pi Imager** : [https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)  
2. Préparez une carte microSD (16 Go minimum recommandé).  
3. Installez **Raspberry Pi OS (64-bit Lite)** dessus.  
4. Démarrez le Raspberry Pi et connectez clavier, écran, alimentation.  
   - Identifiant par défaut : `pi`  
   - Mot de passe : `raspberry`  


## Commandes essentielles

```bash
# Changer le mot de passe par défaut
passwd

# Activer SSH
sudo raspi-config

# Vérifier que SSH fonctionne
systemctl status ssh

# Obtenir l'adresse IP
hostname -I

# Se connecter depuis un autre PC
ssh pi@ADRESSE_IP

# Mise à jour du système
sudo apt update && sudo apt upgrade -y

# Installer les dépendances Python
pip install -r requirements.txt