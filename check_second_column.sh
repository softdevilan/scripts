#!/bin/bash
# Verificar si la segunda columna de un archivo contiene la palabra pepe
read -p "Introduce el nombre del fichero: " fichero

if awk -F: '$2 ~ /pepe/' "$fichero"; then
    echo "La segunda columna contiene la palabra pepe"
else
    echo "La segunda columna no contiene la palabra pepe"
fi
