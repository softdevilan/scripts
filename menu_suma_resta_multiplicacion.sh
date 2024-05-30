#!/bin/bash
# Menú con opciones de suma, resta y multiplicación
while true; do
    echo "Selecciona una opción:"
    echo "1) Suma"
    echo "2) Resta"
    echo "3) Multiplicación"
    echo "4) Salir"
    read -p "Introduce el número de tu elección: " opcion

    if [ $opcion -eq 4 ]; then
        break
    fi

    read -p "Introduce el primer número: " num1
    read -p "Introduce el segundo número: " num2

    case $opcion in
        1) echo "La suma es: $((num1 + num2))" ;;
        2) echo "La resta es: $((num1 - num2))" ;;
        3) echo "La multiplicación es: $((num1 * num2))" ;;
        *) echo "Opción no válida" ;;
    esac
done
