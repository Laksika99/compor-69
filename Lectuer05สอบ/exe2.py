def generate_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(generate_prime_numbers(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(generate_prime_numbers(10))  # Output: [2, 3, 5, 7]
print(generate_prime_numbers(1))   # Output: []
print(generate_prime_numbers(2))  # Output: [2]