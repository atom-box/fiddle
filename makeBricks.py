# makeBricks.py
# source: https://codingbat.com/prob/p118406

# We want to make a row of bricks that 
# is goal inches long. We have a number 
# of small bricks (1 inch each) and big 
# bricks (5 inches each). Return True if 
# it is possible to make the goal by 
# choosing from the given bricks. This is 
# a little harder than it looks and can 
# be done without any loops. 

def built_wall(g, s):
    total_size =  g * 5 + s * 1
    print('   and this size is ' +  str(total_size))
    return total_size

def make_bricks(inventory_bigs, inventory_smalls, length_wanted):
    for i in range(inventory_bigs):
        for j in range(inventory_smalls):
            print('Wanted is ' + str(length_wanted))

            if length_wanted == built_wall(i, j):
                return True
    return False

print(make_bricks(3, 1, 8)) # True
print(make_bricks(3, 1, 9)) # False
print(make_bricks(3, 2, 10)) # True