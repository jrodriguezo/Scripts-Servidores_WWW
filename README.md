# Despliegue de servidores web con Apache mediante scripts escritos en Python

![p2-screenshot](https://user-images.githubusercontent.com/36509669/51669339-8b24b300-1fc4-11e9-8070-643afb297bae.JPG)

Pasos a realizar:
 - **python3 Autom_VirtualMachine.py** en un host anfitrión
 - **sudo virsh console 'name'** // 'name' = Servidor (si se ha configurado así)
 - cdps@cdps dentro sudo -s para root@cdps 
 - copiar los ficheros Instalapache.py y Addwebhost.py con:  **scp 'fichero' cdps@192.168.122.241:.** 
(ver ifconfig, puede cambiar la dirección IP. No olvidarse de los dos puntos y el punto al final de la sentencia)
 - Dentro de la MV(Máquina Virtual): desde ~# (que es donde se habrán guardado) ejecutar: 
    - **python3 Instalapache.py**
    - **python3 Addwebhost.py 'parámetro'**         //el parámetro es el nombre lógico para acceder a la web que le queremos dar a la dirección IP. Así si se quiere acceder como www.dominio1.cdps, hacer 'parametro' = dominio1
                                                  
