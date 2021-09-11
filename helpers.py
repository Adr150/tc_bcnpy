import requests
from xml.etree import ElementTree
import urllib3


urllib3.disable_warnings()


def consultar_dia(anio,mes,dia):
    # Cabecera, si usara xml soap como cabecera el servidor arroja un error de tipo
    headers = { "content-Type": "text/xml; charset=utf-8"}

    # Consulta soap
    body = f"""<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><RecuperaTC_Dia xmlns="http://servicios.bcn.gob.ni/"><Ano type="xsd:integer">{anio}</Ano><Mes type="xsd:integer">{mes}</Mes><Dia type="xsd:integer">{dia}</Dia></RecuperaTC_Dia></soap:Body></soap:Envelope>"""
    
    # Verify = evita problemas de autenticacion  
    r = requests.post("https://servicios.bcn.gob.ni/Tc_Servicio/ServicioTC.asmx?WSDL", data=body, headers=headers, verify=False)
    response =  r.text

    # Convertir string a XML https://docs.python.org/3/library/xml.etree.elementtree.html
    pyXML=ElementTree.fromstring(response)

    # Usamos los [] para movernos dentro de la estructura XML los niveles se toman como listas
    data = pyXML[0][0][0]

    # Diccionario de respuesta
    response_data = {
        'fecha': f'{anio}-{mes}-{dia}',
        'tc': data.text
    }

    return response_data

def consultar_mes(anio,mes):
    # Lista de fechas y tipos de cambio
    response_data = []

    # Cabecera, si usara xml soap como cabecera el servidor arroja un error de tipo
    headers = { "content-Type": "text/xml; charset=utf-8"}
    # Consulta soap
    body = f"""<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><RecuperaTC_Mes xmlns="http://servicios.bcn.gob.ni/"><Ano>{anio}</Ano><Mes>{mes}</Mes></RecuperaTC_Mes></soap:Body></soap:Envelope>"""
    
    # Verify = evita problemas de autenticacion 
    r = requests.post("https://servicios.bcn.gob.ni/Tc_Servicio/ServicioTC.asmx?WSDL", data=body, headers=headers, verify=False)
    response =  r.text
    
    # Convertir string a XML https://docs.python.org/3/library/xml.etree.elementtree.html
    pyXML=ElementTree.fromstring(response)

    # Usamos los [] para movernos dentro de la estructura XML los niveles se toman como listas
    for x in pyXML[0][0][0]:
        for i in x:
            # Guardamos fecha y tipo de cambio. Existen tres campos mas que son año, mes y dia por separado
            temp = {
                'fecha':i[0].text,
                'tc':i[1].text,
                }
            response_data.append(temp)
    response_data = sorted(response_data, key = lambda fecha : fecha["fecha"])

    return response_data

