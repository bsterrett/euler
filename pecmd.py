#!/usr/bin/python
import sys
import re

def cprint(*args):
    # custom print function
    cprint = print_all

def print_all(*args):
    string = ""
    for arg in args: string += str(arg)
    print string

def print_errors(*args):
    string = ""
    re1 = re.compile('Error:\s?',re.IGNORECASE)
    if re1.match(args[0]) != None:
        for arg in args[1:]: string += str(arg)
        print string

def print_errors_warnings(*args):
    string = ""
    re1 = re.compile('[Error|Warning]:\s?',re.IGNORECASE)
    if re1.match(args[0]) != None:
        for arg in args[1:]: string += str(arg)
        print string

def print_errors_warnings_info(*args):
    string = ""
    re1 = re.compile('[Error|Warning|Info]:\s?',re.IGNORECASE)
    if re1.match(args[0]) != None:
        for arg in args[1:]: string += str(arg)
        print string

def init_print(verbose):
    if verbose == 4:
        cprint = print_all
    elif verbose == 3:
        cprint = print_errors_warnings_info
    elif verbose == 2:
        cprint = print_errors_warnings
    elif verbose == 1:
        cprint = print_errors
    else:
        print("Error: ","Didn't know what level of printing to set!")

def parse_args():
    # Parses command line arguments

    profiling=False
    verbose=2 #1=,2=warning,3=info,4=all
    execute_list=[]

    n1 = re.compile('[\d]') #has a number or range
    n2 = re.compile('[\d]+[\-][\d]+') #is a range
    n3 = re.compile('[\d]+(,[\d]+)+') #is a list
    n4 = re.compile('[\d]+,?\Z') #is a single number

    m1 = re.compile(',\s?') #list
    m2 = re.compile('-') #range


    def remove_duplicates(list):
        #removes all duplicate items from a list
        seen = set()
        seen_add = seen.add
        return [ x for x in list if x not in seen and not seen_add(x) ]

    for arg in sys.argv[1:]:
        cprint("Info: ",arg)
        if arg == "-a" or arg == "--all" or arg == "all":
            cprint("Info: ","Using useless -a flag")
        elif arg == "-p" or arg == "profile":
            profiling = True
            cprint("Info: ","Profiling set to True")
        elif arg == "-v" or arg == "--verbose":
            verbose = 3
            init_print(verbose)
            cprint("Info: ","Verbose level set to 3")
        elif n1.match(arg) != None:
            cprint("Info: ","Found a number or range: ", n1.match(arg).group())
            if n2.match(arg) != None:
                cprint("Info: ","Found a range: ", n2.match(arg).group())
                split = m2.split(arg)
                if len(split) == 2:
                    [exec_range_min, exec_range_max] = [int(split[0]), int(split[1])]
                else:
                    cprint("Error: ","This range isn't valid: ", arg)
                    sys.exit(1)
                cprint("Info: ","Translated to range(",exec_range_min,",",exec_range_max,"+1)")
                if exec_range_max > exec_range_min and exec_range_min >= 1:
                    execute_list += range(exec_range_min,exec_range_max+1)
                else:
                    cprint("Error: ","This range isn't valid: ", arg)
                    sys.exit(1)
            elif n3.match(arg) != None:
                cprint("Info: ","Found a list: ", n3.match(arg).group())
                split = m1.split(arg)
                for string in split:
                    if re.match('\d+',string): execute_list += [int(string)]
            elif n4.match(arg) != None:
                cprint("Info: ","Found a single number: ", n4.match(arg).group())
                execute_list += [int(n4.match(arg).group())]
            else:
                cprint("Error: ","Didn't know how to handle this number!")
                sys.exit(1)
            cprint(execute_list)
        else:
            cprint("Error: ","Didn't understand this input!", arg)
            #sys.exit(1)

    if len(execute_list) > 0:
        execute_list = remove_duplicates(execute_list)
        for solution in execute_list:
            cprint("Info: ","Try to execute this solution somehow: ", solution)
    else:
        cprint("Info: ","Try to gather a list of all solutions to execute them.")

def execute_all_solutions(profiling=False):
    # try to execute all solutions
    pass

def execute_specific_solutions(solutions_list, profiling=False):
    for solution in solutions_list:
        if not profiling:
            # run solution's main()
            pass
        else:
            # run solutions's profile()
            pass


def main():
    parse_args()
    init_print(2)
    print_errors_warnings("Error: ","Something!")
    print_errors_warnings.re1 = re.compile('[Error|Warning]:\s?',re.IGNORECASE)

if __name__ == '__main__':
    main()

