#!/bin/bash
# Saludar a cuatro personas introducidas por el usuario
for i in {1..4}; do
    read -p "Introduce el nombre de la persona $i: " nombre
    echo "Hola, $nombre"
done
