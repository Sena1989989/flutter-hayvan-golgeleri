#!/bin/bash
# Hayvan Golgeleri - Linux/Mac Shell Script
# This script makes it easy to run the program on Linux/Mac

echo "================================================"
echo "HAYVAN GÖLGELERİ (Animal Shadows)"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "HATA: Python3 yüklü değil!"
    echo "ERROR: Python3 is not installed!"
    echo ""
    echo "Python3'ü yüklemek için / To install Python3:"
    echo "  Ubuntu/Debian: sudo apt-get install python3"
    echo "  Mac: brew install python3"
    echo ""
    exit 1
fi

# Run the program
python3 hayvan_golgeleri.py "$@"

echo ""
echo "Çalıştırma tamamlandı! (Execution completed!)"
