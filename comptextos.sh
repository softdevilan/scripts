#!/bin/bash
# Comparar dos cadenas de texto introducidas por teclado
read -p "Introduce la primera cadena: " cadena1
read -p "Introduce la segunda cadena: " cadena2
if [ "$cadena1" == "$cadena2" ]; then
    echo "Las cadenas son iguales"
else
    echo "Las cadenas son diferentes"
fi
