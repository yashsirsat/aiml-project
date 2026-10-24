@echo off
title HomeValue - House Price Prediction
cd /d "%~dp0"
echo ==========================================
echo   HomeValue - House Price Prediction
echo ==========================================
where py >nul 2>nul
if errorlevel 1 (
  echo Python was not found. Install Python 3.11 or 3.12 from https://www.python.org/downloads/
  echo During installation, tick "Add Python to PATH".
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" (
  echo Creating a private Python environment...
  py -3 -m venv .venv
  if errorlevel 1 (echo Could not create environment. Check Python installation.& pause & exit /b 1)
)
echo Installing required packages. This may take a few minutes the first time...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (echo Package installation failed. Check your internet connection and try again.& pause & exit /b 1)
echo.
echo Website starting. Keep this window open.
echo Open http://127.0.0.1:5000 in your browser.
".venv\Scripts\python.exe" app.py
pause
