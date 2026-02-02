#!/data/data/com.termux/files/usr/bin/bash
pkg update && pkg upgrade -y
pkg install python -y
pip install flask
echo "✅ Tudo pronto! Agora rode: python main.py"
