def exists_word(word, instance):
    word = word.lower()
    search = []
    line = 1
    for index in range(len(instance)):
        file_search = instance.search(index)

        expected_result = {
            "palavra": word,
            "arquivo": file_search["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for _ in file_search["linhas_do_arquivo"]:
            if word in _.lower():
                expected_result["ocorrencias"].append({"linha": line})
                search = [expected_result]
            line += 1

    return search


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
