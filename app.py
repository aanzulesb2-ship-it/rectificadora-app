# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
import os  # <-- ¡IMPORTANTE! Añade esta línea

app = Flask(__name__)

# Datos de ejemplo para la galería
gallery_items = [
    {"path": "uploads/motor1.jpg", "type": "image", "comment": "Motor rectificado"},
    {"path": "uploads/video1.mp4", "type": "video", "comment": "Proceso en acción"},
    {"path": "uploads/motor2.jpg", "type": "image", "comment": "Motor ensamblado"},
    {"path": "uploads/video2.mp4", "type": "video", "comment": "Prueba dinámica"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/gallery')
def get_gallery():
    return jsonify(gallery_items)

# --- BLOQUE CORREGIDO PARA PRODUCCIÓN (RENDER) ---
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usa el puerto de Render o 5000 local
    app.run(host='0.0.0.0', port=port)  # ¡Escucha en todas las interfaces!