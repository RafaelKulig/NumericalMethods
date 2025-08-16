# NumericalMethods

## Description
A Python project for implementing and experimenting with numerical methods.

## Features
Currently, the project includes the following numerical method:

- **Bisection Method**: Implements the bisection algorithm for finding roots of continuous functions.

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
3. Run the main script
    ```bash
    python main.py
    ```
### Example Output
```text
Root: 2.0000000000000004, Iterations: 7
```
## Example Usage

The [`Solutions`](Methods/Solutions.py#L4) class provides a `bisection` method for finding roots of equations:

```python
from Methods import Solutions

def main():
    root, iterations=Solutions().bisection(lambda x: x**2 - 4, 0, 5, 0.01, 100)
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
* Fixed Point Method
* Newton Method
* Newton-Raphson Method
* Secant Method

## License

This project is for educational purposes.