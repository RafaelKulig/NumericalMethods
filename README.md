# NumericalMethods

## Description
A Python project for implementing and experimenting with numerical methods.

## Features
Currently, the project includes the following numerical method:

- **Bisection Method**: Implements the bisection algorithm for finding roots of continuous functions.
- **Fixed point**: Implements the fixed point algorithm for finding roots of continuous functions.

## Requirements
- Python 3.x
- No external libraries required

## Usage

1. Clone the repository and navigate to the project folder.
2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows
    ```

## Example Usage

The [`Solutions`](Methods/Solutions.py#L4) class provides the `bisection` and `fixed point` method for finding roots of equations:

```python
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
```

## Project Structure
```plaintext
NumericalMethods/
├── bin/
├── include/
├── lib/
├── lib64/
├── Methods/
│   ├── __pycache__/
│   ├── __init__.py
│   └── Solutions.py
├── main.py

```

## Future Improvements
Planned numerical methods to implement in the project:
* Brent method
* Halley method
* User input on desired error calculation
* Linear system algorithms 

## License

This project is for educational purposes.