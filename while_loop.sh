#!/bin/bash
# Leer datos de teclado hasta pulsar un "0"
while true; do
    read -p "Introduce un valor (0 para salir): " valor
    if [ "$valor" -eq 0 ]; then
        break
    fi
    echo "Has introducido: $valor"
done
