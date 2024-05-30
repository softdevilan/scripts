#!/bin/bash
# Comprobar si estamos en el día 17 del mes
dia=$(date +%d)
if [ "$dia" -eq 17 ]; then
    echo "Hoy es día 17"
else
    echo "Hoy no es día 17"
fi
