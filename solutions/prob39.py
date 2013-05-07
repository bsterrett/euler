#!python

def count_right_triangles(perimeter):
    count = 0
    for a in range(1,perimeter):
        for b in range(perimeter-a,a,-1):
            c = perimeter-a-b
            if a**2 + b**2 == c**2:
                count += 1
    return count
    
if __name__ == '__main__':
    max_triangles = -1
    best_perimeter = -1
    for i in range(4,1001,4):
        triangles = count_right_triangles(i)
        if triangles > max_triangles:
            max_triangles = triangles
            best_perimeter = i
    print "Best perimeter: ", best_perimeter