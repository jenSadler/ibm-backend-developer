#!/bin/bash

filename="./data/raw_data_"
datedFilename="${filename}_$(date +"%Y%m%d")"

today="$(date +"%a %d %b")"
tomorrow=$(date -v+1d +"%a %d %b")

wget -O $datedFilename wttr.in/Casablanca
 if [ $? -eq 0 ]
    then
      grep °C $datedFilename > ./data/temperatures.txt
      bs_tmp=$(head -1 ./data/temperatures.txt | tr -s " " | xargs | rev | cut -d " " -f2 | rev)

      cut -d '│' -f 3 ./data/temperatures.txt | tr -s " " | cut -d "│" -f3 > ./data/noon_temp.txt
      noon_tomorrow=$(head -2 ./data/noon_temp.txt | tail -1 | tr -s " " | xargs | rev | cut -d " " -f2 | rev)
      echo "$noon_tomorrow"
   else
    echo "error downloading files"
fi
