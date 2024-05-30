#!/bin/bash
# Obtener la resta de dos números entrados por teclado
read -p "Introduce el primer número: " num1
read -p "Introduce el segundo número: " num2
resta=$((num1 - num2))
echo "La resta de $num1 y $num2 es: $resta"
