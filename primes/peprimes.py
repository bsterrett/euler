#!python
import re
import time
import sys
try:
    import os
    (primes_dir,success) = re.subn('(.*projecteuler/primes)(/peprimes.py[c]?)','\\1',os.path.realpath(__file__))
    if success > 0:
        cached_primes = True
        sys.path.insert(0,primes_dir)
        import peprimes
    else:
        print "Problem forming primes directory name"
except:
    print "Warning: couldn't add cached primes directory"

class CachedPrimeWorker:
    def __init__(self):
        self.prime_index_file = primes_dir + '/prime_index.txt'
        self.prime_library_file = primes_dir + '/prime_library.txt'
        self.step_size = sys.maxsize/10

    def set_step_size(self,size):
        if size >= 10:  self.step_size = size

    def write_cache_to_file(self):
        if not hasattr(self, "primes"):
            print "Error: primes have not been generated yet!"
            return
        elif len(self.primes) == 0:
            print "Error: no primes to write to library file!"
            return

        row_length = 20
        try:
            index = open(self.prime_index_file, "w")
            index.write("Smallest prime: %s\nLargest prime: %s\nPrimes stored: %s\n" % \
                (self.primes[0], self.primes[-1], len(self.primes)))
            index.close()
        except IOError:
            print "There was a problem writing to the primes index file"

        try:
            library = open(self.prime_library_file, "w")
            for i in range(0,len(self.primes),row_length):
                row = ""
                for j in range(i,min(i+row_length,len(self.primes))):
                    row += str(self.primes[j]) + " "
                library.write(row + "\n")
            library.close()
        except IOError:
            print "There was a problem writing to the primes library file"

    def import_primes_from_file(self, upper_bound = -1):
        try:
            library = open(self.prime_library_file, "r")
            self.primes = []
        except IOError:
            print "There was a problem reading from the primes library file"
            print self.prime_library_file
            return

        self.init_from_file = True
        if upper_bound == -1:
            for line in library.readlines():
                self.primes += map(int, line.strip().split(' '))
            self.cached_count = len(self.primes)
            self.cached_bound = self.primes[-1]
        else:
            for line in library:
                self.primes += map(int, line.strip().split(' '))
                if self.primes[-1] >= upper_bound:
                    self.cached_count = len(self.primes)
                    self.cached_bound = self.primes[-1]
                    library.close()
                    return
            if self.primes[-1] < upper_bound:
                print "Warning: primes library did not reach upper bound"
                self.cached_count = len(self.primes)
                self.cached_bound = self.primes[-1]
        library.close()

    def check_cached_count(self):
        if not hasattr(self, "cached_count"):
            print "getting cached count"
            index = open(self.prime_index_file, "r")
            lines = index.readlines()
            index.close()
            for line in lines:
                (count,found) = re.subn('Primes stored: (\d+)\\n','\\1',line)
                if found > 0:
                    self.cached_count = int(count)
        return self.cached_count

    def check_cached_bound(self):
        if not hasattr(self, "cached_bound"):
            index = open(self.prime_index_file, "r")
            lines = index.readlines()
            index.close()
            for line in lines:
                (bound,found) = re.subn('Largest prime: (\d+)\\n','\\1',line)
                if found > 0:
                    self.cached_bound = int(bound)
        return self.cached_bound

    def generate_primes_by_bound(self,upper_bound):
        start_time = time.time()

        self.init_from_file = False
        primes = []
        for i in range(2,upper_bound+1,self.step_size):
            step_bound = min(i+self.step_size,upper_bound+1)
            prime_dict = dict()
            new_primes = []
            for j in range(i,step_bound):  prime_dict[j] = True
            for j in primes:
                for k in range(j,step_bound,j): prime_dict[k] = False
            for j in range(i,step_bound):
                if prime_dict[j] == True:
                    new_primes.append(j)
                    k = range(j,step_bound,j)
                    for l in k[1:]:
                        prime_dict[l] = False
            primes += new_primes
        self.cached_count = len(primes)
        self.cached_bound = primes[-1]
        self.primes = primes
        return time.time() - start_time

    def generate_primes_by_count(self,count):
        start_time = time.time()

        self.init_from_file = False
        primes = []
        i = 2
        while(len(primes) < count):
            step_bound = min(i+self.step_size,upper_bound+1)
            prime_dict = dict()
            new_primes = []
            for j in range(i,step_bound):  prime_dict[j] = True
            for j in primes:
                for k in range(j,step_bound,j): prime_dict[k] = False
            for j in range(i,step_bound):
                if prime_dict[j] == True:
                    new_primes.append(j)
                    k = range(j,step_bound,j)
                    for l in k[1:]:
                        prime_dict[l] = False
            primes += new_primes
            i += self.step_size
        self.cached_count = len(primes)
        self.cached_bound = primes[-1]
        print "elapsed time:", time.time() - start_time
        self.primes = primes

    def get_primes(self):
        return self.primes

    def check_primality(self,number):
        try:
            if number <= self.cached_bound:
                #this number is a prime
                self.primes.index(number)
                return True
            print "Error: number exceeds cache bound"
            return False
        except ValueError:
            #number was not in list of primes
            return False
        except AttributeError:
            #something was not initialized yet
            print "Error: need to initialize primes first"
            return False



if __name__ == '__main__':
    CPW = CachedPrimeWorker()
    #CPW.import_primes_from_file()
    CPW.generate_primes_by_bound(100000000)
