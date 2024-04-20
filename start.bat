chcp 65001
@echo off
setlocal

set "file=first_run.txt"

for /f %%i in (%file%) do set content=%%i
if "%content%"=="1" (
pip install -r requirements.txt
echo 0 > %file%
)
endlocal

python main.py