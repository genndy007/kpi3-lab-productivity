class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Cache(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.cache = []

    def add(self, el):
        self.cache.append(el)

    def clear(self):
        self.cache.clear()

    def is_empty(self):
        return not bool(self.cache)


if __name__ == "__main__":
    c = Cache()
    c.add(1)
    c.clear()
    print(c.is_empty())
