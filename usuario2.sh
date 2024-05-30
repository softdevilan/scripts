#!/bin/bash
# Mostrar las líneas del archivo /etc/passwd que contienen el nombre de usuario introducido por teclado
read -p "Introduce el nombre de usuario: " usuario
grep "$usuario" /etc/passwd
