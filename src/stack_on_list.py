from typing import Union
from src.errors import EmptyError

class Stack:
    def __init__(self) -> None:
        """
        Функция инициализирует пустой стек
        return: None
        """
        self.items: list[Union[int, float, str]] = []


    def is_empty(self) -> bool:
        """
        Функция проверяет, является ли стек пустым
        :return: True если стек пустой, False если нет
        """
        return not self.items


    def push(self, x: Union[int, float, str]) -> None:
        """
        Функция добавляет элемент в конец стека
        :param x: элемент, который нужно добавить
        :return: None
        """
        self.items.append(x)


    def pop(self) -> Union[int, float, str]:
        """
        Функция удаляет из конца стека элемент и возвращает его
        :return: последний элемент стека, который удалили или None (если ошибка - стек пустой)
        """
        if self.is_empty():
            raise EmptyError("Stack is empty")
        else:
            return self.items.pop()


    def peek(self) -> Union[int, float, str]:
        """
        Функция возвращает элемент в конце стека, но не удаляет его
        :return: элемент в конце стека или None (если ошибка - стек пустой)
        """
        if self.is_empty():
            raise EmptyError("Stack is empty")
        else:
            return self.items[-1]


    def __len__(self) -> int:
        """
        Функция возвращает количество элементов в стеке
        :return: количество элементов в стеке
        """
        return len(self.items)
