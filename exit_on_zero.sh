#!/bin/bash
# Introducir números o letras hasta presionar 0 para salir
while true; do
    read -p "Introduce un valor (0 para salir): " valor
    if [ "$valor" -eq 0 ]; then
        break
    fi
    echo "Has introducido: $valor"
done
