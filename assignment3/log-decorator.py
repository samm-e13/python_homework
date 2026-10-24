#Task1: 
import logging

# one time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args,**kwargs):
        logger.log(logging.INFO, f"function: {func.__name__}")
        if args:
            logger.log(logging.INFO, f"Positional Parameter: {args}")
        else:
            logger.log(logging.INFO, f"Positional Parameters: None")

        if kwargs:
            logger.log(logging.INFO, f"Keyword Parameters: {kwargs}")
        else:
            logger.log(logging.INFO, "Keyword Parameters: None")
        solution = func(*args,**kwargs)
        logger.log(logging.INFO, f"Return: {solution}")
        return solution
    return wrapper

@logger_decorator
def test1():
    print("Hello, WOrld!")
test1()

@logger_decorator
def test2(*args):
    return True
test2(3,2)

@logger_decorator
def test3(**kwargs):
    return logger_decorator
test3(name = "roy", age = 18)




