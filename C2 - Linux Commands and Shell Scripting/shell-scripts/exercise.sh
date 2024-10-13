#!/bin/bash

echo "Do you like puppies?"
exit=false
read puppyAffinity

while [ "$exit" == false ]
do
    if [[ "$puppyAffinity" == "Yes" || "$puppyAffinity" == "yes" || "$puppyAffinity" == "Y" || "$puppyAffinity" == "y" ]] 
    then
        echo -e "Yeah, puppies are great. \nHow many do you want?"

        read howMany

        endDogLoop=false

        while [ "$endDogLoop" == false ]
        do
            if [ "$howMany" -gt 0 ] && [ $howMany -lt 5 ]
            then
                echo -e "That's a perfect number of dogs"
                endDogLoop=true;
            elif [ "$howMany" -eq 0 ]
            then
                echo -e "Aww, come on, that's no fun. \nHow many really?"
                read howMany
            elif [ "$howMany" -gt 4 ]
            then
                echo -e "Oh man,that's pushing it, are you sure you don't want to try again?\n\n How many dogs do you want?"
                read howMany
            elif [ "$howMany" -lt 0 ]
            then
                echo -e "Does that mean you're going to give ME dogs? How many dogs do you want?"
                read howMany
            fi
        done

        exit=true
    elif [[ "$puppyAffinity" == "No" || "$puppyAffinity" == "no" || "$puppyAffinity" == "N" || "$puppyAffinity" == "n" ]] 
    then
        echo "oh man, you're missing out"
        exit=true
    else
        echo -e "I don't understand, I asked if you like puppies \nPlease give me a yes or no answer.\n\nDo you like puppies?"
        read puppyAffinity
    fi
done

