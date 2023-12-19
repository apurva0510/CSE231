from proj04 import get_smallest_co_prime

print("get_smallest_co_prime(26):",get_smallest_co_prime(26))
print("get_smallest_co_prime(210):",get_smallest_co_prime(210))
print("get_smallest_co_prime(90):",get_smallest_co_prime(90))

assert get_smallest_co_prime(26) == 3
assert get_smallest_co_prime(210) == 11
assert get_smallest_co_prime(90) == 7
