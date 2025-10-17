#📃 Text Variables in Python
# Strings are used to store text data in Python.
#-----------------------------
text_1 = "text in python is called string"
text_2 = "You can use single quotes ' ' or double quotes \" \" to define a string."
text_3 = "You can use double quotes \" \" inside single quotes ' ' without escaping them by using backslash /."

#🙈 Printing statement
#-----------------------------
print(text_1)
print(text_2)
print(text_3)
print(text_3)
# One of syntax rules of python is you must write text in quotes.
# If you forget to use quotes, python will give you an error.

# Emoji syntax
## use window key + . (dot) to open emoji panel in windows
print("Hello 😊")  # prints Hello with a smiley emoji

#📚 Basic Data-Types in Python
#-----------------------------
# Python has several built-in data types to store different kinds of data.


# 1. Integer (int): Used to store whole numbers (both positive and negative).
int_var = 10
print("Integer value:", int_var)
# 2. Float (float): Used to store decimal numbers.
float_var = 10.5
print("Float value:", float_var)
# 3. String (str): Used to store text data.
str_var = "Hello, World!"
print("String value:", str_var)
# 4. Boolean (bool): Used to store True or False values.
bool_var = True
print("Boolean value:", bool_var)
#  NoneType: Used to represent the absence of a value.
none_var = None
print("NoneType value:", none_var)

# 5. List (list): Used to store a collection of items in a specific order.
list_var = [1, 2, 3, "apple", "banana"]
print("List value:", list_var)
# 6. Tuple (tuple): Similar to lists, but immutable (cannot be changed after creation).
tuple_var = (1, 2, 3, "apple", "banana")
print("Tuple value:", tuple_var)    
# 7. Dictionary (dict): Used to store key-value pairs.
dict_var = {"name": "Alice", "age": 25}
print("Dictionary value:", dict_var)
# 8. Set (set): Used to store a collection of unique items.
set_var = {1, 2, 3, "apple", "banana"}
print("Set value:", set_var)
# These are some of the most commonly used data types in Python.

#📖 F{string}

print(f"String value: {str_var}, Integer value: {int_var}, Float value: {float_var}, Boolean value: {bool_var}, NoneType value: {none_var}, List value: {list_var}, Tuple value: {tuple_var}, Dictionary value: {dict_var}, Set value: {set_var}")