# Chankro
Herramienta para evadir disable_functions y open_basedir. Permite generar un PHP que ejecutará un binario o script que se le pase como input.

Ejemplo:

python chankro.py --arch 64 --input rev.sh --output chan.php --path /var/www/html
