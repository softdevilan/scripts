#!/bin/bash
# Comprobar si la entrada es una letra mayúscula, minúscula o un número
read -p "Introduce un carácter: " char
if [[ "$char" =~ [A-Z] ]]; then
    echo "Has introducido una letra mayúscula"
elif [[ "$char" =~ [a-z] ]]; then
    echo "Has introducido una letra minúscula"
elif [[ "$char" =~ [0-9] ]]; then
    echo "Has introducido un número"
else
    echo "El carácter introducido no es una letra ni un número"
fi
