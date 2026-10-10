@echo off
setlocal
cd /d "%~dp0"
echo Installing/checking PyInstaller...
py -m pip install -r requirements-build.txt
if errorlevel 1 (
  echo Build failed. Check that Python and pip are installed.
  pause
  exit /b 1
)
echo Building Windows executable...
py -m PyInstaller --onefile --name integrity_demo --clean --noconfirm integrity_demo.py
if errorlevel 1 (
  echo Build failed.
  pause
  exit /b 1
)
echo.
echo Windows executable created: dist\integrity_demo.exe
echo See README.md for usage and final ZIP instructions.
pause
