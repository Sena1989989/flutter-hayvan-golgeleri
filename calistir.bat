@echo off
REM Hayvan Golgeleri - Windows Batch Script
REM This script makes it easy to run the program on Windows

echo ================================================
echo HAYVAN GOLGELERI (Animal Shadows)
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo HATA: Python yuklu degil!
    echo ERROR: Python is not installed!
    echo.
    echo Python'u yuklemek icin / To install Python:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Run the program
python hayvan_golgeleri.py %*

REM Pause to see output
echo.
pause
