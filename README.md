# oslib

Una libreria Python leggera, veloce e affidabile per ottenere informazioni sul dispositivo e fornire utility di sistema.

---

## Installazione

Installa la libreria con pip:

```bash
pip install oslib
```

Verifica che l'installazione sia andata a buon fine:

```bash
python -c "import oslib; print('si.')"
```

Se il comando stampa:

```text
si.
```

la libreria è installata correttamente.

---

## Esempi d'utilizzo

### Informazioni sul sistema operativo

```python
from oslib import sys_info

os_tag = sys_info.get_platform_tag()

print(os_tag)
# Esempio output:
# windows-x64
```

---

### Utility per i percorsi

```python
from oslib import path_utils

path = ("C:\\", "Windows", "System32", "..", "Temp")

normalized_path = path_utils.normalize(path)

print(normalized_path)
# Output:
# C:\Windows\Temp
```

---

## Caratteristiche

* Rilevamento del sistema operativo e dell'architettura.
* Utility per normalizzare e gestire i percorsi.
* API semplice e intuitiva.
* Compatibile con Windows, Linux e macOS.
* Leggera e senza dipendenze inutili.

---

## Licenza

Distribuita sotto licenza MIT.
