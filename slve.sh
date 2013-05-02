#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Usage: slve.sh <problem number>"
    exit 1
fi


if [ -d "solutions" ]; then
	cd solutions
    if [[ "all" -ne "$1" && "$1" -gt 0 ]]; then
        #execute a single solution
        number=$1
        solution=prob${number}.py
        if [ -e $solution ]; then
            printf "Working on solution %d\n" $number
            start_time=`date +%s`
            /bin/python $solution
            end_time=`date +%s`
            printf "Execution time was %d seconds\n\n" `expr $end_time - $start_time`
            
        else
            printf "Error: solution %d was not found\n" $number
        fi
    else
        #execute all solutions
        echo "Executing all solutions"
        for number in {1..200}
        do
            solution=prob${number}.py
            if [ -e $soltuion ]; then
                printf "Working on solution %d\n" $number
                start_time=`date +%s`
                /bin/python $solution
                end_time=`date +%s`
                printf "Execution time was %d seconds\n\n" `expr $end_time - $start_time`
            fi
        done
    fi
else
	echo "Error: solutions directory not found"
    exit 1
fi
