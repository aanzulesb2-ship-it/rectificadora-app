# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify

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

if __name__ == '__main__':
    app.run(debug=True, port=8001)

