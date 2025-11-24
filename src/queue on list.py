from typing import Union
from src.errors import Empty

class Queue:
    def __init__(self) -> None:
        """
        Функция инициализирует пустую очередь
        return: None
        """
        self.items: list[Union[int, float, str]] = []


    def is_empty(self) -> bool:
        """
        Функция проверяет, является ли очередь пустой
        :return: True если очередь пустая, False если нет
        """
        return self.items == []


    def enqueue(self, x: Union[int, float, str]) -> None:
        """
        Функция добавляет элемент в конец очереди
        :param x: элемент, который нужно добавить
        :return: None
        """
        self.items.append(x)


    def dequeue(self) -> Union[int, float, str]:
        """
        Функция удаляет из начала очереди элемент и возвращает его
        :return: первый элемент очереди, который удалили или None (если ошибка - очередь пустая)
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            return self.items.pop(0)


    def __len__(self) -> int:
        """
        Функция возвращает количество элементов в очереди
        :return: количество элементов в очереди
        """
        return len(self.items)


    def front(self) -> Union[int, float, str]:
        """
        Функция возвращает элемент в начале очереди, но не удаляет его
        :return: элемент в начале очереди None (если ошибка - очередь пустая)
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            return self.items[0]
