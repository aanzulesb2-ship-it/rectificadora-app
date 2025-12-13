# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import List, Optional
from flask import Flask, render_template
import webbrowser

# ------------------------ Modelos ------------------------
@dataclass
class Person:
    name: str
    role: str
    bio: str
    photo_path: Optional[str] = None
    career: Optional[str] = None  # Para pasantes
    info_tecnica: Optional[str] = None  # Información técnica

@dataclass
class NewsItem:
    title: str
    description: str

@dataclass
class AppState:
    persons: List[Person] = field(default_factory=list)
    news: List[NewsItem] = field(default_factory=list)

# ------------------------ Flask ------------------------
flask_app = Flask(__name__)
app = AppState()

# ------------------------ Datos de ejemplo ------------------------
app.persons.extend([
    Person(name="Ing. Marco Suarez", role="Ingeniero de Taller", bio="Responsable del diagnóstico técnico", photo_path="img/marco.jpg", info_tecnica="Diagnóstico avanzado de motores y calibración CNC."),
    Person(name="Sra. Laura Perez", role="Gerente General", bio="Gestión administrativa", photo_path="img/laura.jpg", info_tecnica="Optimización de procesos y supervisión de calidad."),
    Person(name="Sr. Juan Torres", role="Tecnico Especializado", bio="Experto en rectificado y calibración de motores", photo_path="img/juan.jpg", info_tecnica="Rectificado de precisión, análisis de tolerancias."),
    Person(name="Sr. Pedro Diaz", role="Tecnico Cabezotes", bio="Especialista en cabezotes", photo_path="img/pedro.jpg"),
    Person(name="Sr. Luis Martinez", role="Tecnico Motores Diesel", bio="Experto en motores diesel", photo_path="img/luis.jpg"),
    Person(name="Ana Gomez", role="Pasante", bio="Estudiante de Mecánica", career="Ingeniería Mecánica", photo_path="img/ana.jpg"),
    Person(name="Carlos Vega", role="Pasante", bio="Estudiante de Electromecánica", career="Electromecánica", photo_path="img/carlos.jpg")
])

app.news.extend([
    NewsItem(title="Nueva Maquina CNC", description="Se ha incorporado nueva máquina de precisión.")
])

# ------------------------ Rutas ------------------------
@flask_app.route("/")
def index():
    principales = [p for p in app.persons if "Ingeniero" in p.role or "Gerente" in p.role or "Especializado" in p.role]
    return render_template("index.html", principales=principales)

@flask_app.route("/personal")
def show_personal_web():
    tecnicos = [p for p in app.persons if "Tecnico" in p.role]
    pasantes = [p for p in app.persons if "Pasante" in p.role]
    return render_template("personal.html", tecnicos=tecnicos, pasantes=pasantes)

@flask_app.route("/innovaciones")
def show_innovations():
    return render_template("innovaciones.html", news=app.news)

@flask_app.route("/contacto")
def show_contact():
    return render_template("contacto.html")

# ------------------------ Servidor ------------------------
if __name__ == '__main__':
    url = "http://127.0.0.1:10000"
    webbrowser.open(url)
    # Para desarrollo
    flask_app.run(host="0.0.0.0", port=10000, debug=True)
    # Para producción, descomenta la siguiente línea y comenta la de arriba
    # from waitress import serve
    # serve(flask_app, host="0.0.0.0", port=10000)
