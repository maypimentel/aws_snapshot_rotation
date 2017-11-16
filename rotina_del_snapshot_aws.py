#coding: utf-8

import commands
with open("volumes.txt") as origin_file:
    for line in origin_file:
        vol = line.split(':')[0]
        dias = int(line.split(':')[2])
        print ('Verificando backup do volume %s' %vol)
        check = int(commands.getstatusoutput('aws ec2 describe-snapshots --region us-east-1 --output text | grep %s | wc -l | tr -d " \t\r"' %vol)[1])
        
        while ( check > dias ):
        	print 'O Total de snapshots para o volume %s é %s.' %(vol, check)
        	list_snap = commands.getstatusoutput('aws ec2 describe-snapshots --region us-east-1 --output text | grep %s | cut -f6  | tail -n1' %vol)[1]
        	print 'Vai apagar o Snapshot %s' %list_snap
        	commands.getstatusoutput('aws ec2 delete-snapshot --region us-east-1 --snapshot-id %s' %list_snap)
        	check = int(commands.getstatusoutput('aws ec2 describe-snapshots --region us-east-1 --output text | grep %s | wc -l | tr -d " \t\r"' %vol)[1])
        else:
        	print 'O Total de snapshots para o volume %s é %s.' %(vol, check)
        	print 'Não vai apagar o Snapshot'