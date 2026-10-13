#!/usr/bin/env python3

number = __import__('random').randint(-10, 10)

# Uso de sentencias condicionales para evaluar el número
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
