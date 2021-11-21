def monkey_trouble(a, b):
    if a == b:
        return True
    return False

print(monkey_trouble(True, True))  # True
print(monkey_trouble(False, False))  # True
print(monkey_trouble(True, False))  # False

# We have two monkeys, a and b, and the parameters 
# a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or if 
# neither of them is smiling. Return True if we are 
# in trouble.