# Tipo de cambio Banco central de Nicaragua 
Funciones que permiten solicitar el tipo de cambio del Banco central con Python usando requests mediante POST.

Utilizando los XML que estan en la [Pagina del servicio](https://servicios.bcn.gob.ni/Tc_Servicio/ServicioTC.asmx?WSDL) e insertando los datos con variables de python.

## Uso

1. Instalar los requerimientos haciendo 

`pip install -r requirements.txt`
 
2. Guardar el archivo `helpers.py` en tu directorio e importarlo.

`from helpers import consultar_dia, consultar mes`

3. Llamar a la funcion con los parametros.

    - consultar_dia(año,mes,dia)

        `tc_hoy = consultar_dia(2021,9,11)`

    - consultar_mes(año,mes,dia)

        `tc_mes = consultar_dia(2021,9)`

4. Respuesta

    Ambas funciones retornan diccionarios con los campos fecha (yyyy-mm-dd) y tc. En el caso de mes retorna una lista con los diccionarios correspondientes a cada dia.
