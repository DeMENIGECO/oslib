import platform
import socket

"""
Funzioni per tag macchina
"""

def get_platform_tag(macos_silicon_alias=True):
    system = platform.system().lower()
    machine = platform.machine().lower()

    # Normalizzazione architetture
    if machine in ("x86_64", "amd64"):
        arch = "x64"
    elif machine in ("arm64", "aarch64"):
        arch = "arm"
    elif machine.startswith("arm"):
        arch = "arm"
    elif machine in ("i386", "i686", "x86"):
        arch = "x86"
    else:
        arch = machine

    # Normalizzazione OS
    if system == "windows":
        os_name = "windows"
    elif system == "darwin":
        os_name = "macos"
        # distinzione Apple Silicon vs Intel
        if macos_silicon_alias and arch == "arm":
            return "macos-silicon"
    elif system == "linux":
        os_name = "linux"
    else:
        os_name = system

    return f"{os_name}-{arch}"


def get_os_name():
    system = platform.system().lower()

    # Normalizzazione OS
    if system == "windows":
        os_name = "windows"
    elif system == "darwin":
        os_name = "macos"
    elif system == "linux":
        os_name = "linux"
    else:
        os_name = system

    return os_name

def get_system_architecture():
    machine = platform.machine().lower()

    # Normalizzazione architetture
    if machine in ("x86_64", "amd64"):
        arch = "x64"
    elif machine in ("arm64", "aarch64"):
        arch = "arm"
    elif machine.startswith("arm"):
        arch = "arm"
    elif machine in ("i386", "i686", "x86"):
        arch = "x86"
    else:
        arch = machine

    return arch

"""
Funzioni brevi, ma essenziali
"""

def get_os_version():
    return platform.version()

def get_hostname():
    return socket.gethostname()

def get_python_version():
    return platform.python_version()