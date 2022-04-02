import time

from .genetic import run_tournament
start = time.time()
winner = run_tournament(128)
end = time.time()
print("Total time =", end - start)
print(winner)
