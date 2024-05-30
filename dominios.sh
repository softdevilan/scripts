#!/bin/bash
# Listar la información DNS de dos dominios introducidos por teclado
for i in {1..2}; do
    read -p "Introduce el nombre del dominio $i: " dominio
    /usr/bin/host $dominio
done
