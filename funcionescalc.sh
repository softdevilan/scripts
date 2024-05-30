#!/bin/bash
# Calculadora con funciones y menú para operaciones
suma() { echo $(( $1 + $2 )); }
resta() { echo $(( $1 - $2 )); }
multiplicacion() { echo $(( $1 * $2 )); }
division() { echo $(( $1 / $2 )); }

while true; do
    echo "Selecciona una operación:"
    echo "1) Suma"
    echo "2) Resta"
    echo "3) Multiplicación"
    echo "4) División"
    echo "5) Salir"
    read -p "Introduce el número de tu elección: " opcion

    if [ $opcion -eq 5 ]; then
        break
    fi

    read -p "Introduce el primer número: " num1
    read -p "Introduce el segundo número: " num2

    case $opcion in
        1) suma $num1 $num2 ;;
        2) resta $num1 $num2 ;;
        3) multiplicacion $num1 $num2 ;;
        4) division $num1 $num2 ;;
        *) echo "Opción no válida" ;;
    esac
done
