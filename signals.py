import time, random, math, os

def main(s: float, a: float):
    signal: float = s 
    alignment: float = a
    print("Acquiring signal.")
    for t in range(5):
        print(".")
        time.sleep(random.random())
    print("\nSignal found!")
    
    time.sleep(0.5)
    os.system('clear')
    while signal < 100:
        wait_time: float = random.random() / (alignment * 0.01)
        chance: float = random.random()
        signal += random.random()
        num_clamp(signal, 0.0, 100.0)
        num_clamp(wait_time, 0.0, 1.0)
        num_clamp(alignment, 0.0, 100.0)
        if chance > 0.5:
            alignment -= random.random() * 0.1
        print(f"Signal: {truncate_num(signal, 2)}%")
        print(f"Alignment: {truncate_num(alignment, 2)}%")
        print(f"Waiting for: {truncate_num(wait_time, 2)} seconds.")

        time.sleep(wait_time)
        os.system('clear')
        if alignment < 75.0:
            print("Alignment below minimums.")
            break
        if signal >= 100.0:
            print("Download complete.")
            break


def truncate_num(num: float, decimals: int):
    factor = 10 ** decimals
    return math.trunc(num * factor) / factor

def num_clamp(n, min, max):
    if n < min:
        return min
    if n > max:
        return max
    else:
        return n

if __name__ == "__main__":
    main(0.0, 100)
