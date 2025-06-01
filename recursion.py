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

6 + tri_recursion(5) --> 21
5 + tri_recursion(4) --> 15
4 + tri_recursion(3) --> 10
3 + tri_recursion(2) -->  6
2 + tri_recursion(1) -->  3
1 + tri_recursion(0) -->  1
0

