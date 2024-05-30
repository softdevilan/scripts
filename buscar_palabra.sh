#!/bin/bash
# Buscar una palabra en un fichero de texto
read -p "Introduce la palabra a buscar: " palabra
read -p "Introduce el nombre del fichero: " fichero

if grep -q "$palabra" "$fichero"; then
    echo "La palabra '$palabra' se ha encontrado en el fichero '$fichero'."
else
    echo "La palabra '$palabra' no se ha encontrado en el fichero '$fichero'."
fi
