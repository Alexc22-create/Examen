"""
Examen Unidad III 
Autor: [Alejandro Castelar Hernandez]
Fecha: [29 octubre 2025]

Descripción:
Objetivo del examen
Desarrollar una API básica con Flask que permita:

Crear un diccionario de dispositivos de red.
Agregar nuevos dispositivos.
Modificar dispositivos existentes.
Mostrar un listado de todos los dispositivos en formato HTML, 
donde cada dispositivo se muestre en un <div> con nombre, 
descripción y características

Requisitos técnicos

Usar Flask.
Usar un diccionario como estructura principal de almacenamiento.
Implementar al menos tres rutas:

GET /dispositivos_html: muestra todos los dispositivos en HTML.
POST /dispositivos: agrega un nuevo dispositivo.
PUT /dispositivos/<id>: modifica un dispositivo existente.

Ejemplo del Diccionario de dispositivos: 
{
  "id": "router01",
  "nombre": "Router Principal",
  "descripcion": "Router de borde para salida a Internet",
  "ip": "192.168.1.1",
  "mac": "00:1A:2B:3C:4D:5E",
  "ubicacion": "Sala de servidores",
  "tipo": "Router",
  "otros": ""
}

Recuerda tener al menos 3 commits en tu repositorio. 

Para puntos extra
Puedes ocupar css para añadir puntos a tu examen, perzonalizalo con estilos como el siguiente:
<style>
    .dispositivo {
        border: 1px solid #ccc;
        padding: 10px;
        margin: 10px;
    }
</style>

Puntos extra para añador formula en el cmapo de otros
la formula es la siguente: 

último octeto de la IP * 3 + longitud del nombre del dispositivo + ":" + nombre (Cambiando los espacios por _)

"""
from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)

dispositivos = {}

@app.route('/dispositivos_html', methods=['GET'])
def mostrar_dispositivos_html():
    html = ""
    for id, d in dispositivos.items():
        html += f"""
        <div class="dispositivo">
            <strong>ID : {id}</strong><br>
            <b>Nombre:</b> {d['nombre']}<br>
            <b>Descripción:</b> {d['descripcion']}<br>
            <b>IP:</b> {d['ip']}<br>
            <b>MAC:</b> {d['mac']}<br>
            <b>Ubicación:</b> {d['ubicacion']}<br>
            <b>Tipo:</b> {d['tipo']}<br>
            <b>Otros:</b> {d['otros']}
        </div>
        """
    return render_template_string(f"""
    <html>
    <head>
        <title>Dispositivos de Red</title>
        <style>
            .dispositivo {{
                border: 1px solid #ccc;
                padding: 10px;
                margin: 10px;
            }}
        </style>
    </head>
    <body>
        <h1>Lista de Dispositivos</h1>
        {html}
    </body>
    </html>
    """)
    return html

@app.route('/dispositivos', methods=['POST'])
def agregar_dispositivo():
    data=request.get_json()
    nuevo_dispositivo= {data['id']: {
        "nombre": data['nombre'],
        "descripcion": data['descripcion'],
        "ip": data['ip'],
        "mac": data['mac'],
        "ubicacion": data['ubicacion'],
        "tipo": data['tipo'],
        "otros": data['otros']
    }}
    
    dispositivos.update(nuevo_dispositivo)
    return jsonify({"mensaje": "Dispositivo agregado exitosamente"})

@app.route('/dispositivos_mod', methods=['PUT'])
def modificar_dispositivo():
    data=request.get_json()
    id = data.get('id')
    if id not in dispositivos:
        return jsonify({"error": "Dispositivo no encontrado"})
    
    dispositivos[id].update({
        'nombre': data.get('nombre', dispositivos[id]['nombre']),
        'descripcion': data.get('descripcion', dispositivos[id]['descripcion']),
        'ip': data.get('ip', dispositivos[id]['ip']),
        'mac': data.get('mac', dispositivos[id]['mac']),
        'ubicacion': data.get('ubicacion', dispositivos[id]['ubicacion']),
        'tipo': data.get('tipo', dispositivos[id]['tipo']),
        'otros': data.get('otros', dispositivos[id]['otros']),
    })
    
    return jsonify({"mensaje": "Dispositivo modificado exitosamente"})
    
   
if __name__ == '__main__':
    app.run(debug=True)