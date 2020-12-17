# We generally use static methods to create utility functions.

# self study required in this page./
#https://www.bogotobogo.com/python/python_files.php 


class utils:


    # __init() method is called immediately after an instance is created.
    # it takes one parameter, the stream object that we want to use as standard output for the life of the context.
    def __init__(self):
        print('Hello World')

    @staticmethod
    def path_test():
        print('This is static method!')

    def path_testing(self):
        print("haha")

    # def __enter__():
    #     print('how it is used')
