herenegun=$(date --date='2 days ago' +%F)
atzo=$(date -d yesterday +%Y-%m-%d)
gaur=$(date  +%F)

(mkdir /var/tmp/kopiak)2>/dev/null

	if [ ! -d /var/tmp/kopiak/$atzo ]
	then
		(mkdir /var/tmp/kopiak/$atzo)2>/dev/null
	fi

	if [! -d /var/tmp/kopiak/$gaur]
	then
		(mkdir /var/tmp/kopiak/$gaur)2>/dev/null
	fi
	#ikasten aldakorra
	unekoa=$((find /home/ane -name ikasten | tail -n1)2>/dev/null)


rsync -av --progress --compare-dest=/var/tmp/kopiak/$atzo  $unekoa /var/tmp/kopiak/$gaur

echo $gaur 'eguneko babes kopia eginda.'

