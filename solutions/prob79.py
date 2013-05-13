#!python
from pelib import Found,number_as_list,list_as_number

if __name__ == '__main__':

    keylog = [319,680,180,690,129,620,762,689,762,318,368,710,720,710,629,168,\
    160,689,716,731,736,729,316,729,729,710,769,290,719,680,318,389,162,289,162,\
    718,729,319,790,680,890,362,319,760,316,729,380,319,728,716]

    key = []
    try:
        while(True):
            fixed = len(keylog)
            for attempt in keylog:
                list = number_as_list(attempt)
                index = [-1,-1,-1]
                for d in range(0,len(list)):
                    digit = list[d]
                    if key.count(digit) == 0:
                        key.append(digit)
                        index[d] = key.index(digit)
                    else:
                        index[d] = key.index(digit)
                for i in range(1,len(list)):
                    if index[i] < index[i-1]:
                        digit = list[i]
                        key.remove(digit)
                        key.insert(index[i-1],digit)
                        fixed -= 1
            if fixed == len(keylog): raise Found
    except Found:
        print "Shortest key: ", list_as_number(key)
        exit(0)