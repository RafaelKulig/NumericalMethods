from Methods import Solutions

def main():
    root, iterations=Solutions().bisection(lambda x: x**2 - 4, 0, 5, 0.01, 100)
    print(f"Root: {root}, Iterations: {iterations}")


if __name__=="__main__":
    main()