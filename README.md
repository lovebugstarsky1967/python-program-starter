# python-program-starter
Starter for Python App
Python Programm Starter
GitHub-Beschreibung
Python Programm Starter
Entwickelt von ThomasKarner
Ein elegantes, dunkles GUI-Tool zum einfachen Verwalten und Ausführen von Python-Programmen unter Linux. Diese Anwendung löst das Problem, Python-Skripte bequem zu starten und zu verwalten, mit oder ohne Terminal-Fenster.
Hauptfunktionen:

Durchsuchen von Ordnern nach Python-Dateien mit rekursiver Suche
Mehrere Ausführungsmodi:

Terminal-Modus: Öffnet ein Terminal-Fenster für Konsolenprogramme
GUI-Modus: Startet GUI-Anwendungen ohne Terminal im Hintergrund
Direkt-Modus: Führt Programme ohne spezielle Behandlung aus


Desktop-Verknüpfungen erstellen:

Erstellt elegante Starter-Skripte auf dem Desktop
Unterstützt Programme mit oder ohne Terminal
Starter ohne sichtbare Dateiendung


Dunkles Cyborg-Theme für eine moderne, angenehme Benutzeroberfläche

Technische Details:

Entwickelt mit Python und PySide6
Optimiert für Linux-Desktop-Umgebungen (getestet unter Linux Mint Cinnamon)
Intelligente Arbeitsverzeichnisbehandlung für korrekte Ausführung von Programmen
Temporäre Shell-Skripte für zuverlässige Ausführung

Systemanforderungen:

Python 3.6+
PySide6
Linux-Betriebssystem (Ubuntu, Mint, etc.)

Screenshots:
Füge hier einen Screenshot der Anwendung ein
Benutzeranleitung
Installation

Voraussetzungen installieren:
bashKopierenpip install PySide6

Programm herunterladen:
bashKopierengit clone https://github.com/ThomasKarner/python-program-starter.git
cd python-program-starter

Starten:
bashKopierenpython starter.py


Erste Schritte

Python-Programme durchsuchen:

Klicke auf "Durchsuchen" und wähle einen Ordner mit Python-Dateien aus
Alle Python-Dateien (.py) im Ordner und seinen Unterordnern werden angezeigt
Klicke auf "Aktualisieren", um die Liste nach Änderungen zu aktualisieren


Programme ausführen:

Wähle ein Programm aus der Liste aus
Wähle den Ausführungsmodus:

Terminal: Für Programme, die Ein-/Ausgaben im Terminal benötigen
GUI: Für Programme mit eigener grafischer Oberfläche
Direkt: Standard-Ausführung ohne spezielle Behandlung


Klicke auf "Programm starten" oder doppelklicke auf das Programm in der Liste


Desktop-Verknüpfungen erstellen:

Wähle ein Programm aus der Liste
Klicke auf "Desktop-Verknüpfung erstellen"
Gib einen Namen für die Verknüpfung ein
Wähle, ob ein Terminal angezeigt werden soll (Ja/Nein)
Die Verknüpfung wird auf dem Desktop erstellt
Optional: Teste die Verknüpfung direkt nach der Erstellung



Tipps & Tricks

Für GUI-Programme:

Wähle den "GUI"-Modus oder erstelle eine Desktop-Verknüpfung mit "Terminal anzeigen: Nein"
Dies verhindert, dass ein Terminal-Fenster geöffnet wird


Für Skripte mit Eingabeaufforderungen:

Wähle den "Terminal"-Modus oder erstelle eine Desktop-Verknüpfung mit "Terminal anzeigen: Ja"


Bei Ausführungsproblemen:

Bearbeite die erstellten Starter-Skripte auf dem Desktop mit einem Texteditor
Probiere die alternativen Terminal-Befehle, die im Skript kommentiert sind


Arbeitsverzeichnisse:

Die App setzt automatisch das richtige Arbeitsverzeichnis für jedes Programm
Dies ist wichtig für Programme, die relative Pfade oder Ressourcendateien verwenden



Fehlerbehebung

Desktop-Verknüpfung funktioniert nicht:

Rechtsklick auf die Verknüpfung → Eigenschaften → Berechtigung → "Als Programm ausführen" aktivieren
Versuche, das Skript direkt im Terminal zu starten: bash ~/Desktop/ProgrammName


Programm startet nicht:

Überprüfe, ob alle Python-Abhängigkeiten installiert sind
Versuche, das Programm direkt im Terminal zu starten, um Fehlermeldungen zu sehen


Terminal wird nicht gefunden:

In den erzeugten Skripten sind mehrere Terminal-Emulatoren kommentiert
Bearbeite das Skript und aktiviere eine alternative Terminal-Zeile



Anpassungen
Die App verwendet ein dunkles "Cyborg"-Theme, das auf die meisten Desktop-Umgebungen abgestimmt ist. Wenn du das Aussehen ändern möchtest, kannst du die apply_dark_theme()-Methode im Quellcode anpassen.

Ich hoffe, diese App erleichtert dir die Arbeit mit Python-Skripten erheblich! Bei Fragen oder Verbesserungsvorschlägen erstelle gerne ein Issue auf GitHub.
