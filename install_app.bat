python -m PyInstaller --noconfirm --log-level=WARN ^
    --onefile --noconsole ^
    --hidden-import=random ^
    --hidden-import=tkinter ^
    --hidden-import=PIL ^
    --hidden-import=pygame ^
    --hidden-import=ctypes ^
    --add-data  ./resources;resources ^
    --icon=./resources/favicon.ico ^
    La-question-mystere.py