items = [1, 2, 3, 4, "aaaaa"]

for item in items:
    try:
        if isinstance(item, int):
            print(item)
        else:
            # Raise an exception if the item is not an integer
            raise TypeError(f"Expected integer, but got {type(item).__name__}")
    except TypeError as e:
        # Handle the exception by printing a message
        print(e)
