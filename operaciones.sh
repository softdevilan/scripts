#!/bin/bash
# Leer tres valores por teclado y mostrar su suma y multiplicación
read -p "Introduce el primer valor: " valor1
read -p "Introduce el segundo valor: " valor2
read -p "Introduce el tercer valor: " valor3
suma=$((valor1 + valor2 + valor3))
multiplicacion=$((valor1 * valor2 * valor3))
echo "La suma de los valores es: $suma"
echo "La multiplicación de los valores es: $multiplicacion"
