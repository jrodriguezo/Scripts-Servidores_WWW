import sys
import subprocess

#1
fhost = open('/etc/hosts', 'r+') //para las pruebas en local 
fhost.write('\n    192.168.122.241 '+sys.argv[1]+' www.'+sys.argv[1]+'.cdps')
#2
subprocess.call("sudo mkdir /var/www/"+sys.argv[1],shell=True) //creamos la pagina web
 
fileDom1 = open('/var/www/'+sys.argv[1]+'/index.html','w')//creamos la pagina web
fileDom1.write('<html>'+'\n'+'<h1> servidor: <strong>'+sys.argv[1]+'</strong></h1>'+'\n'+'</html>'+'\n')
fileDom1.close()


#3 //creamos los archivos de configuración para cada uno de los VirtualHost
subprocess.call(['sudo','cp','/etc/apache2/sites-available/000-default.conf','/etc/apache2/sites-available/'+sys.argv[1]+'.conf'])

fin = open('/etc/apache2/sites-available/000-default.conf', 'r') 
fout = open('/etc/apache2/sites-available/'+sys.argv[1]+'.conf', 'w') 
for line in fin: #line te permite leer cada linea del archivo fin
	if "DocumentRoot" in line :
   		fout.write("DocumentRoot /var/www/"+sys.argv[1]+"\n") //ruta en la cual se encuentra alojada la pagina 
   		fout.write("ServerName "+sys.argv[1]+".cdps"+"\n") //nombre del servidor
   		fout.write("ServerAlias www."+sys.argv[1]+".cdps"+"\n") //el alias para acceder
	else:
		fout.write(line)


fin.close()
fout.close()

#4
subprocess.call(['sudo','a2ensite',sys.argv[1]+'.conf']) //para utilizar una configuración distinta a la instalada por defecto
subprocess.call(['sudo','apache2','reload']) //rearrancamos para aplicar los cambios


