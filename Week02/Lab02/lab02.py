even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0
positive_int_count = 0

# Good stuff goes here
n_int = 1

while n_int != 0:

    n_str = input("\nInput an integer (0 terminates): ")
    n_int = int(n_str)

    if n_int == 0:
        break

    elif n_int < 0:
        continue

    elif n_int % 2 == 0:
        even_count += 1
        even_sum += n_int
        positive_int_count += 1

    else:
        odd_count += 1
        odd_sum += n_int
        positive_int_count += 1

#Do not change the following lines of code
print("\n")
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)