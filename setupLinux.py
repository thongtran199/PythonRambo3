import sys
import os
from cx_Freeze import setup, Executable

base = None

build_exe_options = {"packages": ["pygame"],
                     "include_files": ["Img", "Sound", "game.py", "network.py", "Bullet.py", "Rambo.py", "Step.py"]}

setup(
    name="server",
    version="1.0",
    description="My server",
    options={"build_exe": build_exe_options},
    executables=[
        Executable("server.py", base=base),
        Executable("client.py", base=base, targetName="client.exe")
    ]
)