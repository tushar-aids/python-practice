# Generator expression vs List comprehension

# List comprehension
squares_list = [x ** 2 for x in range(5)]
print("List Comprehension:", squares_list)

# Generator expression (uses round brackets)
squares_gen = (x ** 2 for x in range(5))
print("Generator Expression:", list(squares_gen))

# Memory efficiency example
import sys
list_mem = sys.getsizeof([x ** 2 for x in range(1000)])
gen_mem = sys.getsizeof((x ** 2 for x in range(1000)))

print("\nList memory (1000 items):", list_mem, "bytes")
print("Generator memory (1000 items):", gen_mem, "bytes")



output:
List Comprehension: [0, 1, 4, 9, 16]
Generator Expression: [0, 1, 4, 9, 16]

List memory (1000 items): ~8856 bytes
Generator memory (1000 items): ~112 bytes
