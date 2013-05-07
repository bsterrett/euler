#!python

if __name__ == '__main__':

    target = 200
    ways = 0
        
    for two_hundred in range(target,-1,-200):
        for hundred in range(two_hundred,-1,-100):
            for fifty in range(hundred,-1,-50):
                for twenty in range(fifty,-1,-20):
                    for ten in range(twenty,-1,-10):
                        for five in range(ten,-1,-5):
                            for two in range(five,-1,-2):
                                ways += 1

    print "Total ways: ", ways
   
    exit(0)
