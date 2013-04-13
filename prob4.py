#!python
import pelib
    
try:
    i_l = []
    j_l = []
    p_l = []
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            p = i*j;
            if pelib.is_palindrome(i*j):
                p_l.append(p)
                i_l.append(i)
                j_l.append(j)
    raise pelib.Found
except pelib.Found:
    ind = p_l.index(max(p_l))
    print p_l[ind], "=", i_l[ind], "*", j_l[ind]
    
pelib.finish_timing()