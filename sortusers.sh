#!/bin/bash
# Mostrar todos los usuarios del sistema, ordenados alfabéticamente
cut -d: -f1 /etc/passwd | sort
