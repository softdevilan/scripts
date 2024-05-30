#!/bin/bash
# Realizar backup completo del directorio /home en un archivo comprimido
fecha=$(date +%Y%m%d)
archivo_backup="/backups/backup_home_$fecha.tar.gz"
tar -czf $archivo_backup /home
echo "Backup completado: $archivo_backup"
