# Generators in Python are a type of iterable, like lists or tuples,
# but they generate values on the fly and do not store them in memory.
# 
# This makes them very memory efficient, especially when dealing with
# large datasets or streams of data.
# 
# Generators are defined using functions that use the yield keyword.

# Key Features of Generators

  # Lazy Evaluation:
    # Generators compute values as they are requested, rather than
    # storing all of them in memory at once.

  # State Retention:
    # A generator function retains its state between each yield,
    # so it can continue where it left off.
  
  # Single Use:
    # Once a generator's values are exhausted, it cannot be
    # reused. You would need to recreate the generator if you want to
    # iterate over the values again.

# Creating Generators

# There are two main ways to create generators:

# Using a Generator Function
# Using a Generator Expression

