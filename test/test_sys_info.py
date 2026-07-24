import platform
import socket

from oslib.sys_info import (
    get_platform_tag, get_os_name, get_system_architecture,
    get_hostname, get_python_version, get_os_version
    )


def test_macos_silicon(monkeypatch):
    monkeypatch.setattr(platform, "system", lambda: "Darwin")
    monkeypatch.setattr(platform, "machine", lambda: "arm64")

    result = get_platform_tag(macos_silicon_alias=False)

    assert result == "macos-arm"



def test_os_name_with_macos(monkeypatch):
    monkeypatch.setattr(platform, "system", lambda: "Darwin")

    result = get_os_name()

    assert result == "macos"

def test_arch_with_arm64(monkeypatch):
    monkeypatch.setattr(platform, "machine", lambda: "arm64")

    result = get_system_architecture()

    assert result == "arm"

def test_hostname_test_with_macbook(monkeypatch):
    monkeypatch.setattr(socket, "gethostname", lambda: "MacBook-Pro")

    result = get_hostname()

    assert result == "MacBook-Pro"

def test_python_312_version_check(monkeypatch):
    monkeypatch.setattr(platform, "python_version", lambda: "3.12.0")

    result = get_python_version()

    assert result == "3.12.0"

def test_os_version_with_macos_ventura(monkeypatch):
    monkeypatch.setattr(platform, "version", lambda: "13.7.8")

    result = get_os_version()

    assert result == "13.7.8"
