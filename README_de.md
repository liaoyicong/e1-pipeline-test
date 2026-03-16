# e1-pipeline-test
E1 vollständiges Pipeline-Test-Repository — automatisch vom E1-Daemon erstellt

## Taschenrechner-Modul

Dieses Repository enthält jetzt ein Python-Taschenrechner-Modul, das grundlegende arithmetische Operationen bereitstellt.

### Funktionen

- **Vier Grundrechenarten**: Addition, Subtraktion, Multiplikation, Division
- **Klassenbasierte Struktur**: klares objektorientiertes Design mit Calculator-Klasse
- **Typvalidierung**: umfassende Eingabevalidierung mit beschreibenden Fehlermeldungen
- **Ordnungsgemäße Fehlerbehandlung**: Schutz vor Division durch Null und Behandlung ungültiger Eingaben
- **Vollständige Dokumentation**: umfassende Docstrings und Beispiele für alle Methoden
- **Typflexibilität**: Unterstützung sowohl für Ganzzahlen als auch für Gleitkommazahlen
- **Rückwärtskompatibilität**: funktionsbasierte API bleibt für bestehenden Code verfügbar
- **Prägnante API**: bietet sowohl klassen- als auch funktionsbasierte Schnittstellen

### Dateien

- `calculator.py` - Haupttaschenrechner-Modul mit allen arithmetischen Funktionen
- `test_calculator.py` - Umfassende Testsuite zur Funktionsverifikation
- `example_usage.py` - Nutzungsbeispiele und Demonstrationen

### Schnelle Nutzung

#### Klassenbasierter Ansatz (empfohlen):
```python
from calculator import Calculator

# Taschenrechner-Instanz erstellen
calc = Calculator()

# Grundoperationen
result = calc.add(5, 3)        # 8
result = calc.subtract(10, 4)  # 6
result = calc.multiply(6, 7)   # 42
result = calc.divide(15, 3)    # 5.0

# Allgemeine Methode
result = calc.calculate('add', 5, 3)  # 8

# Fehlerbehandlung
try:
    result = calc.divide(10, 0)
except ZeroDivisionError as e:
    print(f"Fehler: {e}")  # Fehler: Cannot divide by zero

# Typvalidierung
try:
    result = calc.add("5", 3)  # Wird einen TypeError auslösen
except TypeError as e:
    print(f"Fehler: {e}")  # Fehler: Argument 1 must be a number
```

#### Funktionsbasierter Ansatz (rückwärtskompatibel):
```python
import calculator

# Grundoperationen
result = calculator.add(5, 3)        # 8
result = calculator.subtract(10, 4)  # 6
result = calculator.multiply(6, 7)   # 42
result = calculator.divide(15, 3)    # 5.0

# Allgemeine Funktion
result = calculator.calculate('add', 5, 3)  # 8
```

### Tests Ausführen

```bash
python test_calculator.py
```

### Beispiele

```bash
python example_usage.py
python calculator.py  # Eingebaute Demonstration
```