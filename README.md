# Despliegue de servidores web con scripts escritos en Python


Pasos a realizar:
  ◾ python3 Autom_VirtualMachine.py en un host anfitrión
  ◾ sudo virsh console Servidor (si en la configuración se ha llamado así)
  ◾ cdps@cdps dentro sudo -s para root@cdps 
  ◾ copiar los ficheros Instalapache.py y Addwebhost.py con:  scp <fichero> cdps@192.168.122.241:. 
(ver ifconfig, puede cambiar la dirección IP. No olvidarse de los dos puntos y el punto al final de la sentencia)
  ◾ Dentro de la MV(Máquina Virtual): desde ~# (que es donde se habrán guardado) ejecutar: 
      ◽ python3 Instalapache.py
      ◽ python3 Addwebhost.py <parámetro>         //el parámetro es el nombre asociado que le queremos dar a la dirección IP. 
                                                  //así si se quiere acceder como www.dominio1.cdps, hacer <parametro> = dominio1
                                                  