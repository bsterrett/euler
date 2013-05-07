#!python
from pelib import Found, is_palindrome

if __name__ == '__main__':
    try:
        i_l = []
        j_l = []
        p_l = []
        for i in range(999,99,-1):
            for j in range(999,99,-1):
                p = i*j;
                if is_palindrome(i*j):
                    p_l.append(p)
                    i_l.append(i)
                    j_l.append(j)
        raise Found
        
    except Found:
        ind = p_l.index(max(p_l))
        print "Largest palindrome:", p_l[ind]
        exit(0)
    exit(1)
