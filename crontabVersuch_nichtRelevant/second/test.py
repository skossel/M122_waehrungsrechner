import datetime
from pathlib import Path

# Aktuelle Uhrzeit abrufen
current_time = datetime.datetime.now().strftime("%H:%M:%S")

# HTML-Inhalt mit der aktuellen Uhrzeit erstellen
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Aktuelle Uhrzeit</title>
</head>
<body>
    <h1>Aktuelle Uhrzeit: {current_time}</h1>
</body>
</html>
"""

# HTML-Datei im selben Verzeichnis schreiben
current_dir = Path.cwd()
html_file = current_dir / "index.html"
with open(html_file, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"Die aktuelle Uhrzeit wurde in die {current_time} geschrieben.")