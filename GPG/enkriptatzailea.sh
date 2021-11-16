
echo 'Nor zara? Idatzi zure identifikazio kodea\nKodea: '
read nork
echo 'Norentzat da mezua? Idatzi  bere identifikazio kodea\nKodea: '
read nori

echo 'Zein da zure gako publikoarekin enkriptatuko duzun fitxategia?\nIzena: '
read fitx

echo '----------------------------------------------------------------------------'

echo 'Zure fitxategia sinatu nahi duzu? (B/E)'
read ema
if [ $ema == "B" ]
then
	gpg --output $fitx.sig -u $nork --sign $fitx
	sinadura=$( gpg --output $fitx.sig -u $nork --sign $fitx )
	gpg --encrypt -u $nork -r $nori $fitx.sig
else
	gpg --encrypt -u $nork -r $nori $fitx
fi




