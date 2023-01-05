# Nested function
# calculator.py

def calculator(x, y):
    def add():
        return x + y
    
    def sub():
        return x - y
    
    return (add(), sub())


if __name__ == '__main___':
    print('---print calculation---')
    print(calculator(10, 5))