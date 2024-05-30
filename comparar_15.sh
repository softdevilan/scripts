#!/bin/bash
# Comparar un número con 15
read -p "Introduce un número: " numero

if [ $numero -lt 15 ]; then
    echo "El número es menor que 15"
elif [ $numero -gt 15 ]; then
    echo "El número es mayor que 15"
else
    echo "El número es igual a 15"
fi
