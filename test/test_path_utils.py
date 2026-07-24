import os
import ntpath

from oslib.path_utils import (
    nt_to_posix, posix_to_nt, normalize
)

def test_nt_to_posix_user():
    result = nt_to_posix("C:\\Users\\utente\\documenti\\file.txt")

    assert result == "/home/utente/documenti/file.txt"

def test_nt_to_posix_app():
    result = nt_to_posix("C:\\Program Files\\app\\file.txt")

    assert result == "/opt/app/file.txt"

def test_nt_to_posix_sample():
    result = nt_to_posix("C:\\ciao\\11")

    assert result == "/ciao/11"

def test_posix_to_nt_user():
    result = posix_to_nt("/home/utente/documenti/file.txt")

    assert result == "C:\\Users\\utente\\documenti\\file.txt"

def test_posix_to_nt_app():
    result = posix_to_nt("/opt/app/file.txt")

    assert result == "C:\\Program Files\\app\\file.txt"

def test_posix_to_nt_sample():
    result = posix_to_nt("/ciao/11")

    assert result == "C:\\ciao\\11"


def test_normalizzator(monkeypatch):
    monkeypatch.setattr(os, "name", "nt")
    monkeypatch.setattr(os, "path", ntpath)
    result = normalize("C:\\", "Windows", "SysWOW64", "..", "System32")

    assert result == "C:\\Windows\\System32"
