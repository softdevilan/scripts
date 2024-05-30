#!/bin/bash
# Menú con varias opciones: buscar usuario, multiplicar números, obtener nombres de grupos y salir
while true; do
    echo "Selecciona una opción:"
    echo "1) Buscar usuario"
    echo "2) Multiplicar dos números"
    echo "3) Obtener nombres de grupos"
    echo "4) Salir"
    read -p "Introduce el número de tu elección: " opcion

    case $opcion in
        1)
            read -p "Introduce el nombre del usuario: " usuario
            if id -u "$usuario" >/dev/null 2>&1; then
                echo "El usuario $usuario existe."
            else
                echo "El usuario $usuario no existe."
            fi
            ;;
        2)
            read -p "Introduce el primer número: " num1
            read -p "Introduce el segundo número: " num2
            echo "La multiplicación de $num1 y $num2 es: $((num1 * num2))"
            ;;
        3)
            cut -d: -f1 /etc/group
            ;;
        4)
            break
            ;;
        *)
            echo "Opción no válida"
            ;;
    esac
done
