# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import List, Optional
from flask import Flask, render_template

# ------------------------ Modelos ------------------------
@dataclass
class Person:
    name: str
    role: str
    bio: str
    photo_path: Optional[str] = None
    career: Optional[str] = None  # Para pasantes

@dataclass
class GalleryItem:
    path: str
    comment: str = ''
    is_video: bool = False

@dataclass
class NewsItem:
    title: str
    description: str

@dataclass
class AppState:
    persons: List[Person] = field(default_factory=list)
    gallery: List[GalleryItem] = field(default_factory=list)
    news: List[NewsItem] = field(default_factory=list)

# ------------------------ Flask ------------------------
flask_app = Flask(__name__)  # <-- Esto debe estar antes de cualquier ruta
app = AppState()

# ------------------------ Rutas ------------------------
@flask_app.route("/")
def index():
    return render_template("index.html", persons=app.persons)

@flask_app.route("/personal")
def show_personal_web():
    return render_template("personal.html", persons=app.persons)

@flask_app.route("/innovaciones")
def show_innovations():
    return render_template("innovaciones.html", news=app.news)

@flask_app.route("/contacto")
def show_contact():
    return render_template("contacto.html")

# ------------------------ Datos de ejemplo ------------------------
app.persons.extend([
    Person(name="Ing. Marco Suarez", role="Ingeniero de Taller", bio="Responsable del diagnostico tecnico", photo_path="img/marco.jpg"),
    Person(name="Sra. Laura Perez", role="Gerente General", bio="Gestion administrativa", photo_path="img/laura.jpg"),
    Person(name="Sr. Juan Torres", role="Tecnico Especializado", bio="Experto en rectificado y calibracion de motores", photo_path="img/juan.jpg"),
    Person(name="Sr. Pedro Diaz", role="Tecnico Cabezotes", bio="Especialista en cabezotes", photo_path="img/pedro.jpg"),
    Person(name="Sr. Luis Martinez", role="Tecnico Motores Diesel", bio="Experto en motores diesel", photo_path="img/luis.jpg"),
    Person(name="Ana Gomez", role="Pasante", bio="Estudiante de Mecánica", career="Ingeniería Mecánica", photo_path="img/ana.jpg"),
    Person(name="Carlos Vega", role="Pasante", bio="Estudiante de Electromecánica", career="Electromecánica", photo_path="img/carlos.jpg")
])

app.news.extend([
    NewsItem(title="Nueva Maquina CNC", description="Se ha incorporado nueva maquina de precision.")
])

# ------------------------ Servidor ------------------------
if __name__ == '__main__':
    from waitress import serve
    serve(flask_app, host="0.0.0.0", port=5000)
