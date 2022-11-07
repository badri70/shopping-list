import sys
from Implementation import Operations

def main():
    args = sys.argv[1:]

    file = args[0]
    operation = args[1]

    obj = Operations(file, operation)

    if operation == "add":
        obj.add_products()
    elif operation == "update":
        obj.update()
    elif operation == "delete":
        obj.delete()
    elif operation == "total":
        obj.total()
    else:
        print("Такой операции нет")


if __name__ == "__main__":
    main()

