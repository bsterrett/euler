#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Usage: slve.sh <problem number>"
    exit 1
fi

if [ ! -d "resources" ]; then
    echo "Warning: resources directory not found."
fi

if [ ! -d "results" ]; then
    echo "Warning: results directory not found. Results will not be saved."
fi

if [ ! -d "solutions" ]; then
	echo "Error: solutions directory not found."
    exit 1
else
    cd solutions
fi


if [[ "all" -ne "$1" && "$1" -gt 0 ]]; then
    #execute a single solution
    number=$1
    solution=prob${number}.py
    if [ -x $solution ]; then
        printf "Working on solution %d\n" $number
        start_time=`date +%s`
        /bin/python $solution
        end_time=`date +%s`
        printf "Execution time was %d seconds\n\n" `expr $end_time - $start_time`
        exit 0
    else
        printf "Error: solution %d was not found.\n" $number
        exit 1
    fi
elif [[ "all" -eq "$1" ]]; then
    #execute all solutions
    echo "Executing all solutions!"
    for number in {1..500}
    do
        solution=prob${number}.py
        if [ -x $solution ]; then
            printf "Working on solution %d   ---   " $number
            start_time=`date +%s`
            /bin/python $solution
            end_time=`date +%s`
            printf "Execution time was %d seconds\n\n" `expr $end_time - $start_time`
        fi
    done
    exit 0
else
    echo "Didn't understand input."
    exit 1
fi