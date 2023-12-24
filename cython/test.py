import main
import time

start_vanilla = time.time()
main.prime_finder_vanilla(20000)
end_vanilla = time.time()
print(end_vanilla-start_vanilla)


start_optimized = time.time()
main.prime_finder_optimized(20000)
end_optimized = time.time()
print(end_optimized-start_optimized)

