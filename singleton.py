class DB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if DB._instance is None:
            DB._instance = object.__new__(cls)
        return DB._instance


# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if Singleton._instance is None:
#             Singleton._instance = Singleton.__Singleton('mehdi')
#         return Singleton._instance
#
#     class __Singleton:
#         def __init__(self, name):
#             self.name = name
