

continent_tuple = ("antarctica", "australia", "asia", "africa", "america", "america")

print("continent_tuple:", continent_tuple)

print("continent_tuple[0]:", continent_tuple[0])
print("continent_tuple[1]:", continent_tuple[1])


# ───────────────────────────────────────────────────────────────────────────
# TUPLE UNPACK
# ───────────────────────────────────────────────────────────────────────────

(ice_continent, kangaroo, why_so_huge, wakanda, they_think_its_all_usa, amazonrainforest) = continent_tuple
print("ice_continent:", ice_continent)
print("kangaroo:", kangaroo)
print("why_so_huge:", why_so_huge)
print("wakanda:", wakanda)
print("they_think_its_all_usa:", they_think_its_all_usa)
print("amazonrainforest:", amazonrainforest)

  
(ice_age, *asia_pacific, wakawaka, the_americas_1, the_americas_2) = continent_tuple  
print("ice_age:", ice_age)
print("asia_pacific:", asia_pacific)
print("wakawaka:", wakawaka)
print("the_americas_1:", the_americas_1)
print("the_americas_2:", the_americas_2)

(frozen, wild_animals, weird_foods, saminaminaeheh, *the_americas) = continent_tuple  
print("frozen:", frozen)
print("wild_animals:", wild_animals)
print("weird_foods:", weird_foods)
print("saminaminaeheh:", saminaminaeheh)
print("the_americas:", the_americas)


(*not_emerike, emerike) = continent_tuple  
print("not_emerike:", not_emerike)
print("emerike:", emerike)


# (ice_age, *asia_pacific, wakawaka, *the_americas) = continent_tuple
# SyntaxError: multiple starred expressions in assignment


# ───────────────────────────────────────────────────────────────────────────
# TUPLE MODIFY
# ───────────────────────────────────────────────────────────────────────────

# make a list, manipulate (edit values or add a new value or remove a value), then override

oops_i_made_a_mistake = list(continent_tuple)
oops_i_made_a_mistake[4] = "north america"
oops_i_made_a_mistake[5] = "south america"
continent_tuple = tuple(oops_i_made_a_mistake)
print("continent_tuple:", continent_tuple)

# singe item tuple

t1 = (42,)       # This is a tuple
t2 = ('hello',)  # Also a tuple
t3 = (42)        # Just an int
t4 = 'hi',       #  Tuple without parentheses (still needs comma)

haha_why_is_this_a_continent = "europe",

# oh you can do this. tuple + tuple

continent_tuple += haha_why_is_this_a_continent
print("continent_tuple:", continent_tuple)

# you can delete the entire thing. LOL

del haha_why_is_this_a_continent
# print(haha_why_is_this_a_continent)
# NameError: name 'haha_why_is_this_a_continent' is not defined



# ───────────────────────────────────────────────────────────────────────────
# LIST CONCATENATION
#
# ONLY 1 OPTION: plus sign (+)
# NO APPEND, NO EXTEND
#
# ───────────────────────────────────────────────────────────────────────────
super_tuple = continent_tuple + continent_tuple
print("super_tuple:", super_tuple)


ultra_tuple = continent_tuple * 4
print("ultra_tuple:", ultra_tuple)

# also works like a list:
# len
# negative indexing
# in
