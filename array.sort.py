import random

array = [random.randint(1, 100) for _ in range(15)]
print("Original:", array)

array.sort()
print("Crescente:", array)

array.sort(reverse=True)
print("Decrescente:", array)

strings = ["banana", "maça", "laranja", "uva", "abacaxi"]
print("\nOriginal strings:", strings)

strings.sort()
print("Crescente:", strings)

strings.sort(reverse=True)
print("Decrescente:", strings)
