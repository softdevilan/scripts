#!/bin/bash
# Comprobar si un usuario y un grupo existen en el sistema
read -p "Introduce el nombre del usuario: " usuario
read -p "Introduce el nombre del grupo: " grupo

if id -u "$usuario" >/dev/null 2>&1; then
    echo "El usuario $usuario existe."
else
    echo "El usuario $usuario no existe."
fi

if getent group "$grupo" >/dev/null 2>&1; then
    echo "El grupo $grupo existe."
else
    echo "El grupo $grupo no existe."
fi
