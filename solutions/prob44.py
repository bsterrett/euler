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
            
def main():
    bound = 10000000
    pairs = []
    while(len(pairs) < 1):
        pents = generate_pents(bound)
        pairs = []
        for i in range(0,len(pents)):
            p1 = pents[i]
            for p2 in pents[i+1:]:
                try:
                    dif = p2-p1 #p2 should always be bigger
                    if not (p1+p2) in pents and not dif in pents:
                        pairs.append((p1,p2,dif))
                except ValueError:
                    pass
                    
        bound *= 10
    print "Difference: ", pairs[0][2]
    
if __name__ == '__main__':
    import profile;profile.run('main()')
    #main()
    exit(0)