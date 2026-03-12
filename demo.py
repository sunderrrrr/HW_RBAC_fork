from user import *

ilya = User("Ilya", "ADMIN")
petya = User("Petya", "USER")
vanya = User("Vanya", "GUEST")

print(some_guest_func(vanya))
print("=============")
try:
    print(view_profile(vanya))
except PermissionError as e:
    print(e)
print("=============")
print(view_profile(petya))
print("=============")
print(some_guest_func(ilya))
print("=============")
print(update_role(ilya, petya, "ADMIN"))
print("=============")
update_role(ilya, petya, "USER")
with SudoMode(petya) as su:
    print(update_role(su, vanya, "USER"))

print(petya.get_role())