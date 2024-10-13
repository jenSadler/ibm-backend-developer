#!/bin/bash

##FUNCTIONS ======================================
function operateOnColumns {
    column0=($(cut -d "," -f 1 "$filePath"))
    column1=($(cut -d "," -f 2 "$filePath"))
    column2=($(cut -d "," -f 3 "$filePath"))

    echo -e "first Column: \n ${column0[@]}"

    diffArray=("Difference")

    length=$(( ${#column1[@]} < ${#column2[@]} ? ${#column1[@]} : ${#column2[@]} ))

    for ((i = 1; i < length; i++)); do
        diffArray+=($((${column1[i]} - ${column0[i]})))
    done
    echo "${diffArray[@]}"

    echo "Title:Datacolumns" > ../data/dataColumns.csv

    for ((i = 0; i < length; i++))
    do
    echo ${diffArray[i]}
        str1=$(echo "${column0[i]}" | tr -d '\n')
        str2=$(echo "${column1[i]}" | tr -d '\n')
        str3=$(echo "${column2[i]}" | tr -d '\n')
        str4=$(echo "${diffArray[i]}" | tr -d '\n')
        completeStr="$str1,$str2,$str3,$str4"

        echo $completeStr >> ../data/dataColumns.csv

    done
    echo "check your csv"

}

##MAIN======================================
filePath="../data/arrays_table.csv"


##if file path doesn't exist, check to see if you have wget.
##if you don't have wget, install it using brew
##Use wget to get the file
#
if [ ! -e "$filePath" ]
then
    if ! command -v wget &> /dev/null
    then
        echo "command not found, installing WGET"
        brew install wget
    else
        echo "wget found"
    fi

    wget -O "$filePath" "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/M3/L2/arrays_table.csv"

    if [ $? -eq 0 ]
    then
        cat "$filePath"
        operateOnColumns
    else
        echo "The csv failed to downlod with exit status $?"
    fi

else
    cat "$filePath"
    operateOnColumns
fi


