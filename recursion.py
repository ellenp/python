# ───────────────────────────────────────────────────────────────────────────
# RECURSION
# efficient and mathematically-elegant approach
# 
# ───────────────────────────────────────────────────────────────────────────

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

# 6 + tri_recursion(5) --> 21
# 5 + tri_recursion(4) --> 15
# 4 + tri_recursion(3) --> 10
# 3 + tri_recursion(2) -->  6
# 2 + tri_recursion(1) -->  3
# 1 + tri_recursion(0) -->  1
# 0



import timeit
# print("input: 1", timeit.timeit(lambda: tri_recursion(1), number=1))
# print("input: 2", timeit.timeit(lambda: tri_recursion(2), number=1))
# print("input: 3", timeit.timeit(lambda: tri_recursion(3), number=1))
# print("input: 4", timeit.timeit(lambda: tri_recursion(4), number=1))
# print("input: 5", timeit.timeit(lambda: tri_recursion(5), number=1))
# print("input: 10", timeit.timeit(lambda: tri_recursion(10), number=1))
# print("input: 20", timeit.timeit(lambda: tri_recursion(20), number=1))
# print("input: 50", timeit.timeit(lambda: tri_recursion(50), number=1))

# input: 1 2.3999891709536314e-06
# input: 2 1.6999838408082724e-06
# input: 3 1.9000144675374031e-06
# input: 4 2.0999868866056204e-06
# input: 5 3.6999990697950125e-06
# input: 10 3.5999983083456755e-06
# input: 20 6.100017344579101e-06
# input: 50 1.1500000255182385e-05

# ───────────────────────────────────────────────────────────────────────────
# Linear Recursion
# Time Complexity: O(n)
# ───────────────────────────────────────────────────────────────────────────


def linear_recursion(n):
    print(n)
    if n <= 0:
        return
    linear_recursion(n - 1)

linear_recursion(10)

# linear_recursion(10)
# linear_recursion(9)
# linear_recursion(8)
# linear_recursion(7)
# linear_recursion(6)
# linear_recursion(5)
# linear_recursion(4)
# linear_recursion(3)
# linear_recursion(2)
# linear_recursion(1)
# linear_recursion(0)
#     --> return

def linear_recursion_wo_print(n):
    if n <= 0:
        return
    linear_recursion_wo_print(n - 1)

print("input: 1", timeit.timeit(lambda: linear_recursion_wo_print(1), number=1))
print("input: 2", timeit.timeit(lambda: linear_recursion_wo_print(2), number=1))
print("input: 5", timeit.timeit(lambda: linear_recursion_wo_print(5), number=1))
print("input: 10", timeit.timeit(lambda: linear_recursion_wo_print(10), number=1))
print("input: 20", timeit.timeit(lambda: linear_recursion_wo_print(20), number=1))
print("input: 50", timeit.timeit(lambda: linear_recursion_wo_print(50), number=1))

# input: 1 2.3999891709536314e-06
# input: 2 2.1999876480549574e-06
# input: 5 4.299974534660578e-06
# input: 10 4.2000028770416975e-06
# input: 20 3.5999983083456755e-06
# input: 50 9.300012607127428e-06

# ───────────────────────────────────────────────────────────────────────────
# Binary Recursion
# Time Complexity: O(2^n)
# ───────────────────────────────────────────────────────────────────────────

def binary_recursion(n):
    print(n)
    if n <= 0:
        return
    binary_recursion(n - 1)
    binary_recursion(n - 1)

# binary_recursion(2)
#     binary_recursion(1)
#         binary_recursion(0)
#             --> return
#         binary_recursion(0)
#             --> return
#     binary_recursion(1)
#         binary_recursion(0)
#           --> return
#         binary_recursion(0)
#           --> return

# binary_recursion(3)
#     binary_recursion(2)
#         binary_recursion(1)
#             binary_recursion(0)
#                 --> return
#             binary_recursion(0)
#                 --> return
#         binary_recursion(1)
#             binary_recursion(0)
#               --> return
#             binary_recursion(0)
#               --> return
#     binary_recursion(2)
#         binary_recursion(1)
#             binary_recursion(0)
#                 --> return
#             binary_recursion(0)
#                 --> return
#         binary_recursion(1)
#             binary_recursion(0)
#               --> return
#             binary_recursion(0)
#               --> return


def fib(n):
    print(n)
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# fib(1)
#     --> return

# fib(0)
#     --> return

# fib(2)
#     fib(1)
#         --> return
#     fib(0)
#         --> return

# fib(3)
#     fib(2)
#         fib(1)
#             --> return
#         fib(0)
#             --> return
#     fib(1)
#         --> return

# fib(4)
#     fib(3)
#         fib(2)
#             fib(1)
#                 --> return
#             fib(0)
#                 --> return
#         fib(1)
#             --> return
#     fib(2)
#         fib(1)
#             --> return
#         fib(0)
#             --> return

# fib(5)
#     fib(4)
#         fib(3)
#             fib(2)
#                 fib(1)
#                     --> return
#                 fib(0)
#                     --> return
#             fib(1)
#                 --> return
#         fib(2)
#             fib(1)
#                 --> return
#             fib(0)
#                 --> return
#     fib(3)
#         fib(2)
#             fib(1)
#                 --> return
#             fib(0)
#                 --> return
#         fib(1)
#             --> return


# fib(6)
#     fib(5)
#         fib(4)
#             fib(3)
#                 fib(2)
#                     fib(1)
#                         --> return
#                     fib(0)
#                         --> return
#                 fib(1)
#                     --> return
#             fib(2)
#                 fib(1)
#                     --> return
#                 fib(0)
#                     --> return
#         fib(3)
#             fib(2)
#                 fib(1)
#                     --> return
#                 fib(0)
#                     --> return
#             fib(1)
#                 --> return
#     fib(4)
#         fib(3)
#             fib(2)
#                 fib(1)
#                     --> return
#                 fib(0)
#                     --> return
#             fib(1)
#                 --> return
#         fib(2)
#             fib(1)
#                 --> return
#             fib(0)
#                 --> return


fib0 = fib(0)
print("fib(0)", fib0)
fib1 = fib(1)
print("fib(1)", fib1)
fib2 = fib(2)
print("fib(2)", fib2)
fib3 = fib(3)
print("fib(3)", fib3)
fib4 = fib(4)
print("fib(4)", fib4)
fib5 = fib(5)
print("fib(5)", fib5)
fib6 = fib(6)
print("fib(6)", fib6)