from cx_Freeze import setup, Executable

# Diga ao cx_Freeze para incluir a sua pasta de assets
build_exe_options = {
    "packages": ["pygame", "code"],
    "include_files": [
        "asset/"  # <--- Copia a pasta inteira de assets para o build
    ],
}

setup(
    name='Maybe they are invading',
    version='1.0',
    description='Jogo',
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)
