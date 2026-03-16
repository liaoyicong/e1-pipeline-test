# e1-pipeline-test
Référentiel de test de pipeline complet E1 — créé automatiquement par le démon E1

## Module Calculatrice

Ce référentiel contient maintenant un module de calculatrice Python qui fournit des opérations arithmétiques de base.

### Fonctionnalités

- **Quatre opérations de base** : addition, soustraction, multiplication, division
- **Structure basée sur les classes** : conception orientée objet claire avec classe Calculator
- **Validation de type** : validation d'entrée complète avec messages d'erreur descriptifs
- **Gestion d'erreur appropriée** : protection contre la division par zéro et gestion des entrées invalides
- **Documentation complète** : docstrings complètes et exemples pour toutes les méthodes
- **Flexibilité de type** : prise en charge des entiers et des nombres à virgule flottante
- **Rétrocompatibilité** : l'API basée sur les fonctions reste disponible pour le code existant
- **API concise** : fournit à la fois des interfaces basées sur les classes et sur les fonctions

### Fichiers

- `calculator.py` - Module de calculatrice principal contenant toutes les fonctions arithmétiques
- `test_calculator.py` - Suite de tests complète pour vérifier les fonctionnalités
- `example_usage.py` - Exemples d'utilisation et démonstrations

### Utilisation Rapide

#### Approche basée sur les classes (recommandée) :
```python
from calculator import Calculator

# Créer une instance de calculatrice
calc = Calculator()

# Opérations de base
result = calc.add(5, 3)        # 8
result = calc.subtract(10, 4)  # 6
result = calc.multiply(6, 7)   # 42
result = calc.divide(15, 3)    # 5.0

# Méthode générale
result = calc.calculate('add', 5, 3)  # 8

# Gestion d'erreur
try:
    result = calc.divide(10, 0)
except ZeroDivisionError as e:
    print(f"Erreur: {e}")  # Erreur: Cannot divide by zero

# Validation de type
try:
    result = calc.add("5", 3)  # Lèvera une TypeError
except TypeError as e:
    print(f"Erreur: {e}")  # Erreur: Argument 1 must be a number
```

#### Approche basée sur les fonctions (rétrocompatible) :
```python
import calculator

# Opérations de base
result = calculator.add(5, 3)        # 8
result = calculator.subtract(10, 4)  # 6
result = calculator.multiply(6, 7)   # 42
result = calculator.divide(15, 3)    # 5.0

# Fonction générale
result = calculator.calculate('add', 5, 3)  # 8
```

### Exécuter les Tests

```bash
python test_calculator.py
```

### Exemples

```bash
python example_usage.py
python calculator.py  # Démonstration intégrée
```