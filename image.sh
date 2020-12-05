#bin/zsh

clear
rm *.png
echo "\nHaciendo normal\n"
python3 Grafica.py -c europa
echo "\n"
python3 Grafica.py -c sudamerica
echo "\n"
python3 Grafica.py -c mundo

echo "\nHaciendo con pais\n"
python3 Grafica.py -c europa -p Ecuador
echo "\n"
python3 Grafica.py -p Spain
echo "\n"
python3 Grafica.py -p Japan

echo "\nHaciendo por genero\n"
python3 Grafica.py -c sudamerica -g male
echo "\n"
python3 Grafica.py -p Ecuador -g female
echo "\n"
python3 Grafica.py -c mundo -g male
echo "\n"
python3 Grafica.py -c europa -g female
