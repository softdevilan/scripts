# Crear el script en Python para generar scripts .sh individuales

# Diccionario con el nombre de los archivos y su contenido
scripts = {
    "variables.sh": """#!/bin/bash
# Definir variables y mostrarlas por pantalla
valor1=10
valor2=20
echo "valor1=$valor1"
echo "valor2=$valor2"
""",

    "nombre.sh": """#!/bin/bash
# Leer nombre y apellidos por parámetros y mostrarlos por pantalla
echo "Nombre: $1"
echo "Apellidos: $2 $3"
""",

    "suma.sh": """#!/bin/bash
# Leer 2 valores por parámetros y mostrar su suma
suma=$(( $1 + $2 ))
echo "La suma de $1 y $2 es: $suma"
""",

    "operaciones.sh": """#!/bin/bash
# Leer tres valores por teclado y mostrar su suma y multiplicación
read -p "Introduce el primer valor: " valor1
read -p "Introduce el segundo valor: " valor2
read -p "Introduce el tercer valor: " valor3
suma=$((valor1 + valor2 + valor3))
multiplicacion=$((valor1 * valor2 * valor3))
echo "La suma de los valores es: $suma"
echo "La multiplicación de los valores es: $multiplicacion"
""",

    "leeretc.sh": """#!/bin/bash
# Leer el contenido del directorio /etc y guardarlo en contenidoetc.txt
ls /etc > contenidoetc.txt
""",

    "showfile.sh": """#!/bin/bash
# Mostrar el contenido de los archivos /etc/passwd y /etc/shadow
cat /etc/passwd
cat /etc/shadow
""",

    "usuario.sh": """#!/bin/bash
# Mostrar las líneas del archivo /etc/passwd que contienen el nombre de usuario
grep "$USER" /etc/passwd
""",

    "usuario2.sh": """#!/bin/bash
# Mostrar las líneas del archivo /etc/passwd que contienen el nombre de usuario introducido por teclado
read -p "Introduce el nombre de usuario: " usuario
grep "$usuario" /etc/passwd
""",

    "startfile.sh": """#!/bin/bash
# Mostrar las primeras 3 líneas del archivo /etc/group
head -n 3 /etc/group
""",

    "endfile.sh": """#!/bin/bash
# Mostrar las últimas 3 líneas del archivo /etc/group
tail -n 3 /etc/group
""",

    "startfile2.sh": """#!/bin/bash
# Mostrar las primeras x líneas del archivo /etc/group, siendo x un valor introducido por teclado
read -p "Introduce el número de líneas a mostrar: " x
head -n $x /etc/group
""",

    "sortusers.sh": """#!/bin/bash
# Mostrar todos los usuarios del sistema, ordenados alfabéticamente
cut -d: -f1 /etc/passwd | sort
""",

    "sortgroups.sh": """#!/bin/bash
# Mostrar todos los grupos del sistema, ordenados alfabéticamente (de mayor a menor)
cut -d: -f1 /etc/group | sort -r
""",

    "calc.sh": """#!/bin/bash
# Sencilla calculadora que realiza suma, resta o división de dos operandos dados por teclado
read -p "Introduce el primer número: " num1
read -p "Introduce el segundo número: " num2
read -p "Introduce la operación (suma, resta, division): " operacion
case $operacion in
    suma)
        resultado=$((num1 + num2))
        ;;
    resta)
        resultado=$((num1 - num2))
        ;;
    division)
        resultado=$((num1 / num2))
        ;;
    *)
        echo "Operación no válida"
        exit 1
        ;;
esac
echo "El resultado de la $operacion es: $resultado"
""",

    "comptextos.sh": """#!/bin/bash
# Comparar dos cadenas de texto introducidas por teclado
read -p "Introduce la primera cadena: " cadena1
read -p "Introduce la segunda cadena: " cadena2
if [ "$cadena1" == "$cadena2" ]; then
    echo "Las cadenas son iguales"
else
    echo "Las cadenas son diferentes"
fi
""",

    "compnums.sh": """#!/bin/bash
# Comparar dos números introducidos por teclado
read -p "Introduce el primer número: " num1
read -p "Introduce el segundo número: " num2
if [ $num1 -eq $num2 ]; then
    echo "Los números son iguales"
else
    echo "Los números son diferentes"
fi
""",

    "nettools.sh": """#!/bin/bash
# Mostrar un menú con herramientas de monitorización y ejecutar la seleccionada
echo "Selecciona una herramienta:"
echo "1) top"
echo "2) ps"
echo "3) df"
echo "4) who"
read -p "Introduce el número de tu elección: " opcion
case $opcion in
    1) top ;;
    2) ps ;;
    3) df ;;
    4) who ;;
    *) echo "Opción no válida" ;;
esac
""",

    "dominios.sh": """#!/bin/bash
# Listar la información DNS de dos dominios introducidos por teclado
for i in {1..2}; do
    read -p "Introduce el nombre del dominio $i: " dominio
    /usr/bin/host $dominio
done
""",

    "while_loop.sh": """#!/bin/bash
# Leer datos de teclado hasta pulsar un "0"
while true; do
    read -p "Introduce un valor (0 para salir): " valor
    if [ "$valor" -eq 0 ]; then
        break
    fi
    echo "Has introducido: $valor"
done
""",

    "funcionescalc.sh": """#!/bin/bash
# Calculadora con funciones y menú para operaciones
suma() { echo $(( $1 + $2 )); }
resta() { echo $(( $1 - $2 )); }
multiplicacion() { echo $(( $1 * $2 )); }
division() { echo $(( $1 / $2 )); }

while true; do
    echo "Selecciona una operación:"
    echo "1) Suma"
    echo "2) Resta"
    echo "3) Multiplicación"
    echo "4) División"
    echo "5) Salir"
    read -p "Introduce el número de tu elección: " opcion

    if [ $opcion -eq 5 ]; then
        break
    fi

    read -p "Introduce el primer número: " num1
    read -p "Introduce el segundo número: " num2

    case $opcion in
        1) suma $num1 $num2 ;;
        2) resta $num1 $num2 ;;
        3) multiplicacion $num1 $num2 ;;
        4) division $num1 $num2 ;;
        *) echo "Opción no válida" ;;
    esac
done
""",

    "backup.sh": """#!/bin/bash
# Realizar backup completo del directorio /home en un archivo comprimido
fecha=$(date +%Y%m%d)
archivo_backup="/backups/backup_home_$fecha.tar.gz"
tar -czf $archivo_backup /home
echo "Backup completado: $archivo_backup"
""",

    "usuario_info.sh": """#!/bin/bash
# Leer nombre, apellidos y dni por teclado y mostrarlos
read -p "Introduce tu nombre: " nombre
read -p "Introduce tus apellidos: " apellidos
read -p "Introduce tu DNI: " dni
echo "Nombre: $nombre"
echo "Apellidos: $apellidos"
echo "DNI: $dni"
""",

    "numeros_1_100.sh": """#!/bin/bash
# Mostrar todos los números del 1 al 100
for i in {1..100}; do
    echo $i
done
""",

    "comparar_15.sh": """#!/bin/bash
# Comparar un número con 15
read -p "Introduce un número: " numero

if [ $numero -lt 15 ]; then
    echo "El número es menor que 15"
elif [ $numero -gt 15 ]; then
    echo "El número es mayor que 15"
else
    echo "El número es igual a 15"
fi
""",

    "verificar_directorio.sh": """#!/bin/bash
# Verificar si la palabra entrada es un directorio en /home
read -p "Introduce el nombre del directorio: " dir
if [ -d "/home/$dir" ]; then
    echo "El directorio existe"
else
    echo "El directorio no existe"
fi
""",

    "comprobar_palabra.sh": """#!/bin/bash
# Comprobar si la palabra introducida es "puzzle"
read -p "Introduce una palabra: " palabra
if [ "$palabra" == "puzzle" ]; then
    echo "Has introducido la palabra puzzle"
else
    echo "La palabra introducida no es puzzle"
fi
""",

    "resta.sh": """#!/bin/bash
# Obtener la resta de dos números entrados por teclado
read -p "Introduce el primer número: " num1
read -p "Introduce el segundo número: " num2
resta=$((num1 - num2))
echo "La resta de $num1 y $num2 es: $resta"
""",

    "buscar_palabra.sh": """#!/bin/bash
# Buscar una palabra en un fichero de texto
read -p "Introduce la palabra a buscar: " palabra
read -p "Introduce el nombre del fichero: " fichero

if grep -q "$palabra" "$fichero"; then
    echo "La palabra '$palabra' se ha encontrado en el fichero '$fichero'."
else
    echo "La palabra '$palabra' no se ha encontrado en el fichero '$fichero'."
fi
""",

    "listar_directorios.sh": """#!/bin/bash
# Listar 4 directorios usando un bucle for
for dir in /etc /bin /usr /home; do
    echo "Directorio: $dir"
done
""",

    "menu_suma_resta_multiplicacion.sh": """#!/bin/bash
# Menú con opciones de suma, resta y multiplicación
while true; do
    echo "Selecciona una opción:"
    echo "1) Suma"
    echo "2) Resta"
    echo "3) Multiplicación"
    echo "4) Salir"
    read -p "Introduce el número de tu elección: " opcion

    if [ $opcion -eq 4 ]; then
        break
    fi

    read -p "Introduce el primer número: " num1
    read -p "Introduce el segundo número: " num2

    case $opcion in
        1) echo "La suma es: $((num1 + num2))" ;;
        2) echo "La resta es: $((num1 - num2))" ;;
        3) echo "La multiplicación es: $((num1 * num2))" ;;
        *) echo "Opción no válida" ;;
    esac
done
""",

    "menu_directorios.sh": """#!/bin/bash
# Menú con opciones para crear directorio, listar directorio, editar /etc/passwd y salir
while true; do
    echo "Selecciona una opción:"
    echo "1) Crear directorio"
    echo "2) Listar directorio actual"
    echo "3) Editar /etc/passwd"
    echo "4) Salir"
    read -p "Introduce el número de tu elección: " opcion

    case $opcion in
        1)
            read -p "Introduce el nombre del directorio a crear: " dir
            mkdir -p "$dir"
            echo "Directorio '$dir' creado."
            ;;
        2)
            ls
            ;;
        3)
            nano /etc/passwd
            ;;
        4)
            break
            ;;
        *)
            echo "Opción no válida"
            ;;
    esac
done
""",

    "check_user_group.sh": """#!/bin/bash
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
""",

    "check_current_user.sh": """#!/bin/bash
# Comprobar si el usuario actual del sistema es Pepe
if [ "$USER" == "Pepe" ]; then
    echo "Hola, Pepe"
else
    echo "Adiós"
fi
""",

    "check_day_17.sh": """#!/bin/bash
# Comprobar si estamos en el día 17 del mes
dia=$(date +%d)
if [ "$dia" -eq 17 ]; then
    echo "Hoy es día 17"
else
    echo "Hoy no es día 17"
fi
""",

    "check_second_column.sh": """#!/bin/bash
# Verificar si la segunda columna de un archivo contiene la palabra pepe
read -p "Introduce el nombre del fichero: " fichero

if awk -F: '$2 ~ /pepe/' "$fichero"; then
    echo "La segunda columna contiene la palabra pepe"
else
    echo "La segunda columna no contiene la palabra pepe"
fi
""",

    "start_with_r.sh": """#!/bin/bash
# Obtener las líneas del archivo /etc/passwd que comienzan con r
grep '^r' /etc/passwd
""",

    "filter_russia.sh": """#!/bin/bash
# Obtener personas que vienen de Rusia
read -p "Introduce el nombre del fichero: " fichero

awk -F: '$2 ~ /Russia/' "$fichero"
""",

    "check_input.sh": """#!/bin/bash
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
""",

    "exit_on_zero.sh": """#!/bin/bash
# Introducir números o letras hasta presionar 0 para salir
while true; do
    read -p "Introduce un valor (0 para salir): " valor
    if [ "$valor" -eq 0 ]; then
        break
    fi
    echo "Has introducido: $valor"
done
""",

    "greet_people.sh": """#!/bin/bash
# Saludar a cuatro personas introducidas por el usuario
for i in {1..4}; do
    read -p "Introduce el nombre de la persona $i: " nombre
    echo "Hola, $nombre"
done
""",

    "menu_varias_opciones.sh": """#!/bin/bash
# Menú con varias opciones: buscar usuario, multiplicar números, obtener nombres de grupos y salir
while true; do
    echo "Selecciona una opción:"
    echo "1) Buscar usuario"
    echo "2) Multiplicar dos números"
    echo "3) Obtener nombres de grupos"
    echo "4) Salir"
    read -p "Introduce el número de tu elección: " opcion

    case $opcion in
        1)
            read -p "Introduce el nombre del usuario: " usuario
            if id -u "$usuario" >/dev/null 2>&1; then
                echo "El usuario $usuario existe."
            else
                echo "El usuario $usuario no existe."
            fi
            ;;
        2)
            read -p "Introduce el primer número: " num1
            read -p "Introduce el segundo número: " num2
            echo "La multiplicación de $num1 y $num2 es: $((num1 * num2))"
            ;;
        3)
            cut -d: -f1 /etc/group
            ;;
        4)
            break
            ;;
        *)
            echo "Opción no válida"
            ;;
    esac
done
"""
}

# Crear los archivos .sh y escribir el contenido en cada uno
for filename, content in scripts.items():
    with open(filename, 'w') as file:
        file.write(content)
    # Hacer que el script sea ejecutable
    import os
    os.chmod(filename, 0o755)

print("Todos los scripts han sido creados.")

