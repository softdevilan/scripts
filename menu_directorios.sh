#!/bin/bash
# Menú con opciones para crear directorio, listar directorio, editar /etc/passwd y salir
while true; do
    echo "Selecciona una opción:"
    echo "1) Crear directorio"
    echo "2) Listar directorio actual"
    echo "3) Editar /etc/passwd"
    echo "4) Salir"
    read -p "Introduce el número de tu elección: " opcion

    case $opcion in
        1)
            read -p "Introduce el nombre del directorio a crear: " dir
            mkdir -p "$dir"
            echo "Directorio '$dir' creado."
            ;;
        2)
            ls
            ;;
        3)
            nano /etc/passwd
            ;;
        4)
            break
            ;;
        *)
            echo "Opción no válida"
            ;;
    esac
done
