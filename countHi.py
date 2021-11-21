# countHi.py
# source: https://codingbat.com/prob/p167246
# Return the number of times that the 
# string "hi" appears anywhere in the given string.

def count_hi(str):
    hi_count = 0
    for i in range(len(str)-1):
        if "hi" == str[i:(i+2)]: 
            hi_count = hi_count + 1
    return hi_count
    
print(count_hi('MICHIGAN')) # 0
print(count_hi('abc hi ho')) # 1
print(count_hi('ABChi hi')) # 2
print(count_hi('hihi')) # 2

