# ───────────────────────────────────────────────────────────────────────────
# RECURSION
# efficient and mathematically-elegant approach
# 
# ───────────────────────────────────────────────────────────────────────────

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    # print(result)
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
print("input: 1", timeit.timeit(lambda: tri_recursion(1), number=1))    # 0.00011
print("input: 2", timeit.timeit(lambda: tri_recursion(2), number=1))    # 0.00011
print("input: 3", timeit.timeit(lambda: tri_recursion(3), number=1))    # 0.00011
print("input: 4", timeit.timeit(lambda: tri_recursion(4), number=1))    # 0.00011
print("input: 5", timeit.timeit(lambda: tri_recursion(5), number=1))    # 0.00011
print("input: 10", timeit.timeit(lambda: tri_recursion(10), number=1))    # 0.00011
print("input: 20", timeit.timeit(lambda: tri_recursion(20), number=1))    # 0.00011
print("input: 50", timeit.timeit(lambda: tri_recursion(50), number=1))    # 0.00011

input: 1 2.3999891709536314e-06
input: 2 1.6999838408082724e-06
input: 3 1.9000144675374031e-06
input: 4 2.0999868866056204e-06
input: 5 3.6999990697950125e-06
input: 10 3.5999983083456755e-06
input: 20 6.100017344579101e-06
input: 50 1.1500000255182385e-05