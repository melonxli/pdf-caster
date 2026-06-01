@echo off
cd /d "%~dp0"
echo Installing sharp...
call npm install sharp
echo.
echo Compressing images...
call node compress-images.js
echo.
pause
