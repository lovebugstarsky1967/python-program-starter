#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QHBoxLayout, QPushButton, QLabel, QLineEdit,
                              QTreeWidget, QTreeWidgetItem, QFileDialog, QMessageBox,
                              QRadioButton, QInputDialog)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class PythonLauncher(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.folder_path = None
        self.python_files = []
        
        # Hauptfenster einrichten
        self.setWindowTitle("Python Programm Starter")
        self.setGeometry(100, 100, 800, 600)
        
        # Dark Theme anwenden (Cyborg-ähnlich)
        self.apply_dark_theme()
        
        # UI erstellen
        self.create_ui()
        
    def apply_dark_theme(self):
        """Dunkles Theme (Cyborg-ähnlich) für die App anwenden"""
        dark_palette = """
        QWidget {
            background-color: #0F0F0F;
            color: #FFFFFF;
            font-size: 10pt;
        }
        QTreeWidget {
            background-color: #161616;
            alternate-background-color: #1A1A1A;
            color: #FFFFFF;
            border: 1px solid #2E2E2E;
        }
        QTreeWidget::item:selected {
            background-color: #2C2C2C;
        }
        QHeaderView::section {
            background-color: #202020;
            color: #FFFFFF;
            padding: 5px;
            border: 1px solid #2E2E2E;
        }
        QPushButton {
            background-color: #2B5B84;
            color: white;
            padding: 8px;
            border: none;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #3A7CB9;
        }
        QPushButton:pressed {
            background-color: #1C3D5A;
        }
        QPushButton#success {
            background-color: #257134;
        }
        QPushButton#success:hover {
            background-color: #2D8C3F;
        }
        QPushButton#info {
            background-color: #2B5B84;
        }
        QPushButton#info:hover {
            background-color: #3A7CB9;
        }
        QLineEdit {
            background-color: #1A1A1A;
            color: #FFFFFF;
            border: 1px solid #2E2E2E;
            padding: 5px;
            border-radius: 3px;
        }
        QRadioButton {
            color: #FFFFFF;
            spacing: 5px;
        }
        QRadioButton::indicator {
            width: 13px;
            height: 13px;
        }
        QRadioButton::indicator:checked {
            background-color: #2B5B84;
            border: 2px solid #FFFFFF;
            border-radius: 7px;
        }
        QRadioButton::indicator:unchecked {
            background-color: #333333;
            border: 2px solid #AAAAAA;
            border-radius: 7px;
        }
        """
        
        self.setStyleSheet(dark_palette)
        
    def create_ui(self):
        """UI-Elemente erstellen"""
        # Zentrales Widget und Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Überschrift
        header_frame = QWidget()
        header_layout = QVBoxLayout(header_frame)
        header_layout.setContentsMargins(0, 0, 0, 0)
        
        header_label = QLabel("Python Programm Starter")
        header_font = QFont()
        header_font.setPointSize(16)
        header_font.setBold(True)
        header_label.setFont(header_font)
        header_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(header_label)
        
        # Entwickler-Info hinzufügen
        developer_label = QLabel("Entwickelt von ThomasKarner")
        developer_font = QFont()
        developer_font.setPointSize(10)
        developer_font.setItalic(True)
        developer_label.setFont(developer_font)
        developer_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(developer_label)
        
        main_layout.addWidget(header_frame)
        
        # Ordnerauswahl-Bereich
        folder_frame = QWidget()
        folder_layout = QHBoxLayout(folder_frame)
        folder_layout.setContentsMargins(0, 0, 0, 0)
        
        folder_label = QLabel("Ordner:")
        self.folder_entry = QLineEdit()
        browse_button = QPushButton("Durchsuchen")
        browse_button.setObjectName("success")
        refresh_button = QPushButton("Aktualisieren")
        refresh_button.setObjectName("info")
        
        folder_layout.addWidget(folder_label)
        folder_layout.addWidget(self.folder_entry, 1)  # Stretch-Faktor 1
        folder_layout.addWidget(browse_button)
        folder_layout.addWidget(refresh_button)
        
        main_layout.addWidget(folder_frame)
        
        # Liste der Python-Dateien
        files_label = QLabel("Python-Dateien:")
        main_layout.addWidget(files_label)
        
        self.file_tree = QTreeWidget()
        self.file_tree.setHeaderLabels(["Dateiname", "Pfad"])
        self.file_tree.setAlternatingRowColors(True)
        self.file_tree.setColumnWidth(0, 200)
        self.file_tree.setSortingEnabled(True)
        self.file_tree.itemDoubleClicked.connect(lambda item, column: self.run_program(item))
        main_layout.addWidget(self.file_tree, 1)  # Stretch-Faktor 1
        
        # Optionen-Bereich
        options_frame = QWidget()
        options_layout = QVBoxLayout(options_frame)
        options_layout.setContentsMargins(0, 0, 0, 0)
        
        # Radiobuttons für Ausführungsmodi
        radio_frame = QWidget()
        radio_layout = QHBoxLayout(radio_frame)
        radio_layout.setContentsMargins(0, 0, 0, 0)
        
        self.mode_label = QLabel("Ausführungsmodus:")
        radio_layout.addWidget(self.mode_label)
        
        self.mode_terminal = QRadioButton("Terminal")
        self.mode_terminal.setChecked(True)
        radio_layout.addWidget(self.mode_terminal)
        
        self.mode_gui = QRadioButton("GUI-Anwendung")
        radio_layout.addWidget(self.mode_gui)
        
        self.mode_direct = QRadioButton("Direkt")
        radio_layout.addWidget(self.mode_direct)
        
        radio_layout.addStretch(1)
        
        options_layout.addWidget(radio_frame)
        main_layout.addWidget(options_frame)
        
        # Button-Bereich
        button_frame = QWidget()
        button_layout = QHBoxLayout(button_frame)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        # Erstelle Desktopverknüpfung Button
        create_desktop_button = QPushButton("Desktop-Verknüpfung erstellen")
        create_desktop_button.setObjectName("success")
        button_layout.addWidget(create_desktop_button)
        
        button_layout.addStretch(1)  # Platz zwischen Buttons
        
        run_button = QPushButton("Programm starten")
        run_button.setMinimumWidth(150)
        button_layout.addWidget(run_button)
        
        main_layout.addWidget(button_frame)
        
        # Signale und Slots verbinden
        browse_button.clicked.connect(self.browse_folder)
        refresh_button.clicked.connect(self.refresh_files)
        run_button.clicked.connect(self.run_program)
        create_desktop_button.clicked.connect(self.create_desktop_entry)
        
    def browse_folder(self):
        """Öffnet einen Dialog zur Ordnerauswahl"""
        folder = QFileDialog.getExistingDirectory(self, "Ordner auswählen")
        if folder:
            self.folder_path = folder
            self.folder_entry.setText(folder)
            self.refresh_files()
    
    def refresh_files(self):
        """Aktualisiert die Liste der Python-Dateien im ausgewählten Ordner"""
        self.python_files = []
        self.file_tree.clear()
        
        folder_path = self.folder_entry.text()
        if not folder_path or not os.path.isdir(folder_path):
            QMessageBox.critical(self, "Fehler", "Bitte wähle einen gültigen Ordner aus.")
            return
        
        # Python-Dateien finden
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, folder_path)
                    self.python_files.append(full_path)
                    
                    item = QTreeWidgetItem([file, rel_path])
                    self.file_tree.addTopLevelItem(item)
        
        # Nach Dateiname sortieren
        self.file_tree.sortItems(0, Qt.AscendingOrder)
    
    def run_program(self, item=None):
        """Startet das ausgewählte Python-Programm"""
        try:
            # Wenn kein Item übergeben wurde oder es kein QTreeWidgetItem ist
            if item is None or not isinstance(item, QTreeWidgetItem):
                selected_items = self.file_tree.selectedItems()
                if not selected_items:
                    QMessageBox.information(self, "Hinweis", "Bitte wähle ein Python-Programm aus.")
                    return
                item = selected_items[0]
                
            file_name = item.text(0)
            rel_path = item.text(1)
            
            folder_path = self.folder_entry.text()
            full_path = os.path.join(folder_path, rel_path)
            
            # Prüfe, ob die Datei existiert
            if not os.path.exists(full_path):
                QMessageBox.critical(self, "Fehler", f"Die Datei existiert nicht: {full_path}")
                return
                
            # Erstelle ein temporäres Ausführungsskript
            import tempfile
            
            # Erstelle ein temporäres Shell-Skript
            fd, temp_script = tempfile.mkstemp(suffix='.sh')
            
            # Python-Interpreter-Pfad ermitteln
            python_path = "python3"
            try:
                python_result = subprocess.run(['which', 'python3'], 
                                             stdout=subprocess.PIPE, 
                                             text=True)
                if python_result.returncode == 0:
                    python_path = python_result.stdout.strip()
            except:
                pass
                
            # Skript-Inhalt je nach Modus
            if self.mode_terminal.isChecked():
                # Terminal-Modus
                script_content = f"""#!/bin/bash
# Wechsle in das Verzeichnis des Python-Skripts
cd "{os.path.dirname(full_path)}"
# Führe das Python-Skript aus
{python_path} "{os.path.basename(full_path)}"
echo "Programm beendet. Drücke Enter zum Schließen..."
read
"""
                # Schreibe Skript
                with os.fdopen(fd, 'w') as temp:
                    temp.write(script_content)
                
                # Mache Skript ausführbar
                os.chmod(temp_script, 0o755)
                
                # Führe mit Terminal-Emulator aus
                terminal_found = False
                terminal_cmds = [
                    f"gnome-terminal -- '{temp_script}'",
                    f"konsole --noclose -e '{temp_script}'",
                    f"xfce4-terminal --hold -e '{temp_script}'",
                    f"mate-terminal --hold -e '{temp_script}'",
                    f"terminator -e '{temp_script}'",
                    f"xterm -e '{temp_script}'"
                ]
                
                for cmd in terminal_cmds:
                    term_name = cmd.split()[0]
                    try:
                        which_result = subprocess.run(['which', term_name], 
                                                    stdout=subprocess.PIPE, 
                                                    stderr=subprocess.PIPE)
                        if which_result.returncode == 0:
                            subprocess.Popen(cmd, shell=True)
                            terminal_found = True
                            break
                    except:
                        continue
                
                if not terminal_found:
                    # Direktes Ausführen im Terminal
                    QMessageBox.warning(self, "Hinweis", 
                                      "Kein Terminal-Emulator gefunden. Direktes Ausführen im Terminal.")
                    os.system(f"x-terminal-emulator -e '{temp_script}'")
            
            else:
                # GUI oder Direkt-Modus - kein Terminal
                script_content = f"""#!/bin/bash
# Wechsle in das Verzeichnis des Python-Skripts
cd "{os.path.dirname(full_path)}"
# Führe das Python-Skript aus
{python_path} "{os.path.basename(full_path)}"
"""
                # Schreibe Skript
                with os.fdopen(fd, 'w') as temp:
                    temp.write(script_content)
                
                # Mache Skript ausführbar
                os.chmod(temp_script, 0o755)
                
                # Führe direkt aus
                if self.mode_gui.isChecked():
                    # Im Hintergrund ausführen für GUI-Apps
                    subprocess.Popen([temp_script], 
                                   stdout=subprocess.DEVNULL, 
                                   stderr=subprocess.DEVNULL)
                else:
                    # Direkte Ausführung
                    subprocess.Popen([temp_script])
            
            # Bestätigungsmeldung
            mode_name = "Terminal" if self.mode_terminal.isChecked() else "GUI" if self.mode_gui.isChecked() else "Direkt"
            QMessageBox.information(self, "Info", f"Programm gestartet: {file_name} (Modus: {mode_name})")
            
            # Temporäres Skript löschen (nach kurzer Verzögerung)
            def delete_temp_script():
                import time
                time.sleep(2)  # Warte 2 Sekunden
                try:
                    os.remove(temp_script)
                except:
                    pass  # Ignoriere Fehler beim Löschen
            
            # Starte einen Thread zum Löschen des Skripts
            import threading
            threading.Thread(target=delete_temp_script, daemon=True).start()
        
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Starten des Programms:\n{str(e)}")
    
    def create_desktop_entry(self):
        """Erstellt einen einfachen Starter für das ausgewählte Python-Programm"""
        try:
            selected_items = self.file_tree.selectedItems()
            if not selected_items:
                QMessageBox.information(self, "Hinweis", "Bitte wähle ein Python-Programm aus.")
                return
            
            item = selected_items[0]
            file_name = item.text(0)
            rel_path = item.text(1)
            
            folder_path = self.folder_entry.text()
            full_path = os.path.abspath(os.path.join(folder_path, rel_path))
            
            # Existenz prüfen
            if not os.path.exists(full_path):
                QMessageBox.critical(self, "Fehler", f"Die Datei existiert nicht: {full_path}")
                return
            
            # Anwendungsname abfragen
            app_name, ok = QInputDialog.getText(self, "Starter erstellen", 
                                            "Name des Starters:", 
                                            text=os.path.splitext(file_name)[0])
            if not ok or not app_name:
                return
            
            # Terminal-Option abfragen
            terminal_option, ok = QInputDialog.getItem(self, "Terminal-Option", 
                                                  "Terminal anzeigen?", 
                                                  ["Nein", "Ja"], 
                                                  0, False)
            if not ok:
                return
            
            # Desktop-Pfad finden
            desktop_path = None
            possible_paths = [
                os.path.expanduser("~/Desktop"),
                os.path.expanduser("~/Schreibtisch"),
                os.path.expanduser("~/desktop")
            ]
            
            # Versuche XDG-Pfad
            try:
                xdg_result = subprocess.run(['xdg-user-dir', 'DESKTOP'], 
                                          stdout=subprocess.PIPE, 
                                          text=True)
                if xdg_result.returncode == 0:
                    possible_paths.insert(0, xdg_result.stdout.strip())
            except:
                pass
            
            # Prüfe alle möglichen Pfade
            for path in possible_paths:
                if os.path.exists(path) and os.path.isdir(path):
                    desktop_path = path
                    break
            
            if not desktop_path:
                QMessageBox.critical(self, "Fehler", "Desktop-Pfad konnte nicht gefunden werden.")
                return
            
            # Dateinamen und Pfad für den Starter erstellen
            script_filename = f"{app_name.replace(' ', '_')}"  # Keine .sh Endung
            script_path = os.path.join(desktop_path, script_filename)
            
            # Python-Interpreter-Pfad ermitteln
            python_path = "/usr/bin/python3"  # Standard-Pfad
            try:
                python_result = subprocess.run(['which', 'python3'], 
                                             stdout=subprocess.PIPE, 
                                             text=True)
                if python_result.returncode == 0:
                    python_path = python_result.stdout.strip()
            except:
                pass  # Standardwert verwenden
            
            # Skript-Inhalt erstellen - so einfach wie möglich
            if terminal_option == "Ja":
                # Mit Terminal
                script_content = f"""#!/bin/bash
# Starter für: {app_name}
# Ausgangsverzeichnis speichern
ORIG_DIR=$(pwd)
# In das Programmverzeichnis wechseln
cd "{os.path.dirname(full_path)}"
# Terminal öffnen mit dem Python-Programm
gnome-terminal -- {python_path} "{os.path.basename(full_path)}"
# Alternativ auch diese Zeilen probieren (eine nach der anderen auskommentieren):
# xterm -e "{python_path} \\"{os.path.basename(full_path)}\\""
# x-terminal-emulator -e "{python_path} \\"{os.path.basename(full_path)}\\""
# konsole --noclose -e "{python_path} \\"{os.path.basename(full_path)}\\""
# Zurück zum ursprünglichen Verzeichnis
cd "$ORIG_DIR"
"""
            else:
                # Ohne Terminal
                script_content = f"""#!/bin/bash
# Starter für: {app_name}
# Ausgangsverzeichnis speichern
ORIG_DIR=$(pwd)
# In das Programmverzeichnis wechseln
cd "{os.path.dirname(full_path)}"
# Python-Programm direkt ausführen
{python_path} "{os.path.basename(full_path)}" &
# Zurück zum ursprünglichen Verzeichnis
cd "$ORIG_DIR"
"""

            # Skript schreiben
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            # Ausführbar machen
            os.chmod(script_path, 0o755)
            
            # Zum Testen ausführen?
            test_option = QMessageBox.question(self, "Starter testen", 
                                          f"Der Starter wurde erstellt:\n{script_path}\n\n"
                                          f"Möchtest du den Starter jetzt testen?",
                                          QMessageBox.Yes | QMessageBox.No)
            
            if test_option == QMessageBox.Yes:
                subprocess.Popen(['bash', script_path])
                
            QMessageBox.information(self, "Starter erstellt", 
                               f"Der Starter wurde erfolgreich erstellt:\n{script_path}\n\n"
                               "Hinweis: Falls der Starter nicht funktioniert, bearbeite ihn mit einem Texteditor. "
                               "Es sind alternative Befehle im Skript kommentiert, die du aktivieren kannst.")
                
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Erstellen des Starters:\n{str(e)}")


def main():
    app = QApplication(sys.argv)
    window = PythonLauncher()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
