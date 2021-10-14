lehen=$(pwd)
zip=$((sudo find ~/Escritorio -name irudia.zip | head -n2 |tail -n1)2>/dev/null)
cd ~/Escritorio
mkdir irudia
mv $zip irudia
cd irudia
unzip irudia.zip

irudia=$(md5sum *| grep 'e5ed313192776744b9b93b1320b5e268' | cut -d ' ' -f3 | head -n1)

echo -e '\nEzkutuko mezua irakurtzeko 'EXTRACT' sakatu\n'
stegosuite $irudia


