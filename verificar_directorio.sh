#!/bin/bash
# Verificar si la palabra entrada es un directorio en /home
read -p "Introduce el nombre del directorio: " dir
if [ -d "/home/$dir" ]; then
    echo "El directorio existe"
else
    echo "El directorio no existe"
fi
