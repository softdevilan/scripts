#!/bin/bash
# Mostrar las líneas del archivo /etc/passwd que contienen el nombre de usuario
grep "$USER" /etc/passwd
