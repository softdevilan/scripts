#!/bin/bash
# Mostrar las primeras x líneas del archivo /etc/group, siendo x un valor introducido por teclado
read -p "Introduce el número de líneas a mostrar: " x
head -n $x /etc/group
