#!/bin/bash

root_dir=`pwd`
results_dir="${root_dir}/results"
results_file="${results_dir}/results.raw"
slow_solutions_file="${results_dir}/slow_solutions.raw"
solutions_dir="${root_dir}/solutions"

if [[ $# -ne 1 ]]; then
    echo "Usage: slve.sh <problem number>"
    exit 1
fi

if [ ! -d $results_dir ]; then
    mkdir results
fi

if [ ! -d $solutions_dir ]; then
	echo "Error: solutions directory not found."
    exit 1
else
    cd solutions
fi


if [[ "all" -ne "$1" && "$1" -gt 0 ]] ; then
    #execute a single solution
    number=$1
    solution=prob${number}.py
    if [ -x $solution ]; then
        printf "Working on solution %d\n" $number
        start_time=`date +%s`
        output=$(/bin/python $solution)
		exit_status=$?
		echo $output
        end_time=`date +%s` ; time_elapsed=`expr $end_time - $start_time`
        printf "Execution time was %d seconds\n\n" $time_elapsed
        exit 0
    else
        printf "Error: solution %d was not found.\n" $number
        exit 1
    fi
elif [[ "all" -eq "$1" ]] ; then
    #execute all solutions
    echo "Executing all solutions!"
    for number in {1..500}
    do
        solution=prob${number}.py
        if [ -x $solution ]; then
            printf "Working on solution %d   ---   " $number
            start_time=`date +%s`
			output=$(/bin/python $solution)
			exit_status=$?
            echo $output
			output_target_value=`echo "$output" | sed 's|.*:\s*\(-*\d*\b\)|\1|1'`			
			end_time=`date +%s` ; time_elapsed=`expr $end_time - $start_time`
			printf "%s,%d,%s\n" $number $output_target_value $time_elapsed >> "${results_dir}/results.raw"
			if [[ $time_elapsed -gt 20 ]] ; then 
				printf "%s,%d,%s\n" $number $output_target_value $time_elapsed >> "${results_dir}/slow_solutions.raw"
			fi
			printf "Execution time was %d seconds\n\n" $time_elapsed
        fi
    done
    exit 0
else
    echo "Didn't understand input."
    exit 1
fi