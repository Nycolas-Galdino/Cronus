import subprocess

def setup_environment():
    print("Instalando dependências...")
    subprocess.run(["poetry", "install"])

    print("Configuração inicial concluída!")

if __name__ == "__main__":
    setup_environment()
