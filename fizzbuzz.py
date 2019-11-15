for n in range(1,101):
    print("FizzBuzz" if not n%15 else "Fizz" if not n%3 else "Buzz" if not n%5 else n)