# Questo script esegue una pulizia delle seguenti tre cartelle
# By iThinkAle
import os

try:
    os.system('cmd /c "del /q /f /s %temp%\*"') # %temp%
    os.system('cmd /c "del /s /q C:\Windows\temp\*"') # Temp
    os.system('cmd /c "del /s /q C:\Windows\Prefetch"') # Prefetch
except:
    print("pulizia fallita, riprovare")
else:
    print("pulizia completata")