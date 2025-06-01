# ───────────────────────────────────────────────────────────────────────────
# WHILE
# ───────────────────────────────────────────────────────────────────────────

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

i = 1
while i < 6:
  if i == 3: break
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# ───────────────────────────────────────────────────────────────────────────
# FOR
# ───────────────────────────────────────────────────────────────────────────

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
