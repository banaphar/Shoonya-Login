# Shoonya API Login Helper - Termux Setup **By बनाफर**


A Python script to log into the **Shoonya (Finvasia) API** using Termux on Android.  
It automates **TOTP-based 2FA** and initializes your API session.

---

## ⚡ Features

- Logs into Shoonya API automatically  
- Supports **TOTP-based 2FA**  
- Ready-to-run in **Termux environment**  
- Minimal setup required  

## 📋 Requirements

- Android device with **Termux** installed  
- Active internet connection  
- Shoonya API credentials:  
  - `user_id`  
  - `password`  
  - `totp_secret`  

---

## 🛠️ Installation

Open Termux and run the following commands step by step:

```bash
# Update and upgrade Termux packages
apt update
apt upgrade -y

# Install Git and Python
apt install git -y
apt install python -y

# Install required tools
pkg install cmake -y
pkg install clang make -y
pkg install ninja patchelf -y

# Configure PATH if needed
export PATH=$PATH:/data/data/com.termux/files/usr/bin

# Upgrade Python packages and install dependencies
pip install --upgrade pip setuptools wheel
pip install numpy
pip install pandas
pip install PyYAML
pip install norenrestapi
pip install pyotp 
# Clone the Shoonya Login repository
git clone https://github.com/banaphar/Shoonya-Login.git
cd Shoonya-Login
