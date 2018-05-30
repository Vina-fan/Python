# Python from Scratch

## Using Python

The Python interpreter is usually installed as `/usr/bin/python` on those machines where it is available.

- To start a Python interpreter, type the command in your terminal: `python`.

- To terminate the Python interpreter, type an end-of-file character (`Control-D` on Unix, `Control-Z` on Windows) at the primary prompt. If that doesn’t work, you can exit the interpreter by typing the following command: `quit()`.

### Executing Python scripts

1. Write down your pyton scrpt and name it as `hello.py` with `.py` extension

2. Your script contents look like this 

```
#!/usr/bin/python

print('Hello World')
```

3. Go to your terminal, make your script excutable

```
chmod +x hello.py
```

4. Run the script in your terminal

```
./hello.py
```

To start iPython interactive environment, type `ipython` in your terminal.

## Getting help

- Help is available in IPython sessions using `help( function )` . 

- Some functions (and modules) have very longhelp files. When using IPython, these can be paged using the command `? function` or `function ?` so that the text can be scrolled using page up and down and `q` to `quit`. `??function` or `function??` can be used to type the entire function including both the docstring and the code.
