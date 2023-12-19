from proj04 import check_co_prime

print("check_co_prime(2,3):",check_co_prime(2,3))
print("check_co_prime(2,8):",check_co_prime(2,8))

assert check_co_prime(2,3) == True
assert check_co_prime(2,8) == False

