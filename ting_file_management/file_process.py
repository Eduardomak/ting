import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for _ in instance._Queue__queue:
        if _["nome_do_arquivo"] == path_file:
            return
    queue_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file),
    }
    instance.enqueue(queue_dict)
    print(instance.__dict__, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    try:
        path_file = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso")
    except TypeError:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
