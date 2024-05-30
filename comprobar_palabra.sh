#!/bin/bash
# Comprobar si la palabra introducida es "puzzle"
read -p "Introduce una palabra: " palabra
if [ "$palabra" == "puzzle" ]; then
    echo "Has introducido la palabra puzzle"
else
    echo "La palabra introducida no es puzzle"
fi
