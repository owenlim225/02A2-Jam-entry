import random
import time

symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?`~"  # Symbols to glitch
duration = 10  # Glitch duration in seconds

print(''.join(random.choice(symbols) for _ in range(50)), end='', flush=True)
for _ in range(duration * 10):
    print(random.choice(symbols), end='', flush=True)
    time.sleep(0.1)
