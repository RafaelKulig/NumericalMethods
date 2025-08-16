from Methods import Solutions
from math import cos
def main():
    root, iterations=Solutions().bisection(lambda x: x**2 - 4, 0, 3, error=1e-6, max_iter=100)
    print(f"Root: {root}, Iterations: {iterations}")

    # root, iterations=Solutions().bisection(lambda x: x**2 + 1, -1, 1, error=1e-6, max_iter=100)
    # print(f"Root: {root}, Iterations: {iterations}")

    root, iterations=Solutions().fixed_point(lambda x: cos(x),x0=1.0, error=1e-6, max_iter=100)
    print(f"Root: {root}, Iterations: {iterations}")

    # root, iterations=Solutions().fixed_point(lambda x: 2 * x,x0=1.0, error=1e-6, max_iter=50)
    # print(f"Root: {root}, Iterations: {iterations}")

    root, iterations=Solutions().bisection(lambda x: x - 1, 0, 2, error=1e-10, max_iter=100)
    print(f"Root: {root}, Iterations: {iterations}")

if __name__=="__main__":
    main()