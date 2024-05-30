#!/bin/bash
# Mostrar un menú con herramientas de monitorización y ejecutar la seleccionada
echo "Selecciona una herramienta:"
echo "1) top"
echo "2) ps"
echo "3) df"
echo "4) who"
read -p "Introduce el número de tu elección: " opcion
case $opcion in
    1) top ;;
    2) ps ;;
    3) df ;;
    4) who ;;
    *) echo "Opción no válida" ;;
esac
