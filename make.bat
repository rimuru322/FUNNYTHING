if exist "icon.ico" (
        pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --add-data "images;images/"  "main.py"
    ) else (
        pyinstaller --noconfirm --onefile --windowed --add-data "images;images/"  "main.py"
        echo WARNING: icon.ico doesn't exist!
    )