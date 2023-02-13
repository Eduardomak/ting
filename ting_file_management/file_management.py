import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file) as file:
            data = file.readlines()
            required_export = [line.replace("\n", "") for line in data]
            return required_export
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
