#!/bin/bash
# Comprobar si el usuario actual del sistema es Pepe
if [ "$USER" == "Pepe" ]; then
    echo "Hola, Pepe"
else
    echo "Adiós"
fi
