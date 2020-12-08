#bin/zsh

clear
rm *.png
echo "Haciendo por continente"
python3 Grafica.py -c europa
echo ""
python3 Grafica.py -c sudamerica
echo ""
python3 Grafica.py -c mundo

echo "Haciendo con pais"
python3 Grafica.py -p Ecuador
echo "Haciendo por genero"
python3 Grafica.py -c sudamerica -g male
echo ""
python3 Grafica.py -c sudamerica -g female
echo ""
python3 Grafica.py -c europa -g male
echo ""
python3 Grafica.py -c europa -g female
echo ""
python3 Grafica.py -c mundo -g male
echo ""
python3 Grafica.py -c mundo -g female
echo ""
python3 Grafica.py -p Ecuador -g male
echo ""
python3 Grafica.py -p Ecuador -g female

