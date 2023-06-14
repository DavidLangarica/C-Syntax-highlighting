# C# Lexical Highlighter

This repository contains two Python implementations of a C# lexical highlighter. One implementation is for sequential programming, while the other implements parallel programming using the `Pygments` library and `concurrent.futures`.

## Requirements

- Pygments library (`pip install pygments`)

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/DavidLangarica/CSharp-Lexical-Highlighter.git
   ```

2. Place the C# files you want to highlight in the same directory as the Python programs.

3. Sequential Version:

   ```bash
   python sequential_highlighter.py
   ```

4. Parallel Version:

   ```bash
   python parallel_highlighter.py
   ```

5. The highlighted versions of the C# files will be saved with the same names.

## Tools

- [Pygments](https://pygments.org/) - A syntax highlighting library for Python.
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) - A module in Python for parallel programming.
