if exist "icon.ico" (
        pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --add-data "images;images/" --add-data "config.json;."  "main.py"
    ) else (
        pyinstaller --noconfirm --onefile --windowed --add-data "images;images/" --add-data "config.json;."  "main.py"
        echo WARNING: icon.ico doesn't exist!
    )