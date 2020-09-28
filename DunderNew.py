import copy
import random


class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self


class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))


class JavaScriptObject(dict):
    def __getattribute__(self, item):
        try:
            return self(item)
        except KeyError:
            return super().__getattribute__(item)


# Code Challenge example
class Double(int):
    def __new__(self, num):
        return int(num) * 2


class Liar(list):
    pass

    def __len__(self):
        length = super().__len__()
        return length + 5
