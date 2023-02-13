from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.__queue = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.__queue)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.__queue.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if len(self.__queue) == 0:
            return None
        return self.__queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index not in range(len(self.__queue)):
            raise IndexError
        return self.__queue[index]
