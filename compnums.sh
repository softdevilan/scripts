#!/bin/bash
# Comparar dos números introducidos por teclado
read -p "Introduce el primer número: " num1
read -p "Introduce el segundo número: " num2
if [ $num1 -eq $num2 ]; then
    echo "Los números son iguales"
else
    echo "Los números son diferentes"
fi
