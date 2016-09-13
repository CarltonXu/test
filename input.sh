#!/bin/bash
while :
do
# input your name
read -p "Please input your name:" Name
if [ "$Name" = "quit" ]; then
    exit 4
elif [ "$Name" = "exit" ]; then
    exit 4
else
   echo  "You input ${#Name} number...."
fi
done

