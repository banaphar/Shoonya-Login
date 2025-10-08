#!/usr/bin/env bash
pkg update -y && pkg upgrade -y && pkg install -y python clang make cmake ninja patchelf && export PATH=$PATH:/data/data/com.termux/files/usr/bin && pip install --upgrade pip setuptools wheel && pip install numpy pandas PyYAML pyotp NorenRestApiPy norenrestapi
