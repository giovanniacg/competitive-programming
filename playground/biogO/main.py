from tqdm import tqdm
import math

# O(n)
def O_n(N):
    count = 0
    for _ in tqdm(range(N), desc="O(n)", total=N):
        count += 1
    return count

# O(n^2)
def O_n2(N):
    count = 0
    for _ in tqdm(range(N), desc="O(n²)", total=N):
        for __ in range(N):
            count += 1
    return count

# O(n^3)
def O_n3(N):
    count = 0
    for _ in tqdm(range(N), desc="O(n³)", total=N):
        for __ in range(N):
            for ___ in range(N):
                count += 1
    return count

# O(log n)
def O_log_n(N):
    count = 0
    steps = int(math.log2(N)) if N > 1 else 1
    for _ in tqdm(range(steps), desc="O(log n)", total=steps):
        count += 1
    return count

# O(n log n)
def O_n_log_n(N):
    count = 0
    steps = int(math.log2(N)) if N > 1 else 1
    for _ in tqdm(range(N), desc="O(n log n)", total=N):
        for __ in range(steps):
            count += 1
    return count

# O(2^n) - versão com tqdm
def O_2n(N):
    total = 2**N  
    pbar = tqdm(desc="O(2^n)", total=total)

    count = [0]

    def exponential_loop(n):
        count[0] += 1
        pbar.update(1)

        if n == 1:
            return

        exponential_loop(n-1)
        exponential_loop(n-1)

    exponential_loop(N)
    pbar.close()
    return count[0]

if __name__ == "__main__":
    exec_func = O_2n
    n = int(input("Value of N: "))
    print(f"loops: {exec_func(n)}")
