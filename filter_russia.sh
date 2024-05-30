#!/bin/bash
# Obtener personas que vienen de Rusia
read -p "Introduce el nombre del fichero: " fichero

awk -F: '$2 ~ /Russia/' "$fichero"
