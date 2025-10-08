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
apt update
apt upgrade -y
apt install git -y
apt install python -y
pkg install cmake -y
pkg install clang make -y
export PATH=$PATH:/data/data/com.termux/files/usr/bin
pkg install ninja patchelf -y
pip install --upgrade pip setuptools wheel
pip install numpy
pip install pandas
pip install PyYAML
pip install norenrestapi
git clone https://github.com/banaphar/Shoony
a-Login.git
cd Shoonya-Login
