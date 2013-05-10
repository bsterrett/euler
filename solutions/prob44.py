#!python

def generate_pents(upper_bound):
    if not hasattr(generate_pents, "pents") or not hasattr(generate_pents, "pent_iter"):
        pents = [1]
        pent_iter = 4
    
    while(True):
        last = pents[-1]
        if last > upper_bound: return pents
        else:
            pents.append(last + pent_iter)
            pent_iter += 3
 
if __name__ == '__main__':
    bound = 10000000
    pairs = []
    while(len(pairs) < 1):
        pents = generate_pents(bound)
        pairs = []
        for i in range(0,len(pents)):
            p1 = pents[i]
            for p2 in pents[i+1:]:
                if pents.count(p1+p2) > 0 and pents.count(abs(p1-p2)) > 0:
                    pairs.append((p1,p2,abs(p1-p2)))
        bound *= 10
    print "Difference: ", pairs[0][2]