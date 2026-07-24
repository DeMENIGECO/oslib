import os

"""
Utilità di conversioni di percorsi tra NT (Windows) e POSIX (Linux/MacOS)
"""

def posix_to_nt(path):
    # Sostituzioni valide solo all'inizio del percorso
    prefix_substitutions = {
        "/home/": "C:\\Users\\",
        "/opt/": "C:\\Program Files\\",
    }

    # Controlla i prefissi più specifici per primi
    for prefix in sorted(prefix_substitutions, key=len, reverse=True):
        if path.startswith(prefix):
            path = prefix_substitutions[prefix] + path[len(prefix):]
            break
    else:
        # Se il percorso inizia con "/" ma non con un prefisso noto
        if path.startswith("/"):
            path = "C:\\" + path[1:]

    # Converte gli slash rimanenti
    path = path.replace("/", "\\")

    return path

def nt_to_posix(path):
    # Sostituzioni valide solo all'inizio del percorso
    prefix_substitutions = {
        "C:\\Users\\": "/home/",
        "C:\\Program Files\\": "/opt/",
    }

    # Controlla i prefissi più specifici per primi
    for prefix in sorted(prefix_substitutions, key=len, reverse=True):
        if path.startswith(prefix):
            path = prefix_substitutions[prefix] + path[len(prefix):]
            break
    else:
        # Se il percorso inizia con "/" ma non con un prefisso noto
        if path.startswith("C:\\"):
            path = "/" + path[3:]

    # Converte gli slash rimanenti
    path = path.replace("\\", "/")

    return path


"""
Normalizzatore path
"""

import os

def normalize(*parts):
    return os.path.normpath(os.path.join(*parts))

