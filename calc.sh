#!/bin/bash
# Sencilla calculadora que realiza suma, resta o división de dos operandos dados por teclado
read -p "Introduce el primer número: " num1
read -p "Introduce el segundo número: " num2
read -p "Introduce la operación (suma, resta, division): " operacion
case $operacion in
    suma)
        resultado=$((num1 + num2))
        ;;
    resta)
        resultado=$((num1 - num2))
        ;;
    division)
        resultado=$((num1 / num2))
        ;;
    *)
        echo "Operación no válida"
        exit 1
        ;;
esac
echo "El resultado de la $operacion es: $resultado"
