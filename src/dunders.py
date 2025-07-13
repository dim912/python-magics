# dunders are special methods and variables in Python that start and end with double underscores.
# are used by Python to implement certain behaviors and functionalities.

def main():
    print(f"name is {__name__}") # __main__ if run as a script, module name if imported
    print(f"file is {__file__}") # full path to the file
    print(f"doc is {__doc__}") # docstring of the module
    print(f"package is {__package__}") # empty string if not part of a package
    print("\n")


if __name__ == "__main__": #only called if run as a script (py src/dunders.py), not if imported as a module
    main()


main()