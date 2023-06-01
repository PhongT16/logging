import logging

# This sets the root logger
#logging.basicConfig(filename='logging-output.txt', level=logging.INFO, format='%(filename)s:%(levelname)s:%(message)s')

# Custom logger
logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)

formater = logging.Formatter('%(name)s:%(filename)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('logging-out.txt')
file_handler.setFormatter(formater)
#file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


num1 = 10
num2 = 20
logger.warning("num1 + num2 = " + str(add(num1, num2)))
logger.warning("num1 - num2 = " + str(subtract(num1, num2)))
logger.warning("num1 * num2 = " + str(multiply(num1, num2)))
logger.warning("num1 / num2 = " + str(divide(num1, num2)))

