# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import List, Optional
from flask import Flask, render_template
import time

# ------------------------ Data Models ------------------------
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
    show_splash: bool = True
    show_contact: bool = False
    persons: List[Person] = field(default_factory=list)
    gallery: List[GalleryItem] = field(default_factory=list)
    news: List[NewsItem] = field(default_factory=list)

# ------------------------ App Logic ------------------------
class RectificadoraSuarezApp:
    def __init__(self):
        self.state = AppState()
        self.demo_inputs = ['1','3','5','7','8']
        self.input_index = 0

    def start_app(self):
        print("--- GRUPO RECTIFICADORA SUAREZ ---")
        self.show_splash()
        self.main_menu()

    def show_splash(self):
        print("Splash: Bienvenido")
        time.sleep(1)
        self.state.show_splash = False

    def get_choice(self, prompt: str) -> str:
        try:
            return input(prompt).strip()
        except:
            if self.input_index < len(self.demo_inputs):
                choice = self.demo_inputs[self.input_index]
                print(f"{prompt}{choice} (simulado)")
                self.input_index += 1
                time.sleep(0.3)
                return choice
            return '8'

    def main_menu(self):
        while True:
            print("\n--- Menu Principal ---")
            print("1. Mostrar Personal")
            print("2. Agregar Personal")
            print("3. Galeria")
            print("4. Agregar Imagen/Video")
            print("5. Noticias")
            print("6. Agregar Noticia")
            print("7. Contacto")
            print("8. Salir")
            choice = self.get_choice("Selecciona una opcion: ")
            if choice == '1':
                self.show_personal()
            elif choice == '2':
                self.add_person()
            elif choice == '3':
                self.show_gallery()
            elif choice == '4':
                self.add_gallery_item()
            elif choice == '5':
                self.show_news()
            elif choice == '6':
                self.add_news()
            elif choice == '7':
                self.toggle_contact()
            elif choice == '8':
                print("Saliendo...")
                break
            else:
                print("Opcion no valida.")

    def show_personal(self):
        if not self.state.persons:
            print("No hay personal registrado.")
            return
        for p in self.state.persons:
            print(f"{p.name} ({p.role}): {p.bio}")

    def add_person(self):
        print("Funcion de agregar personal disponible en modo interactivo")

    def show_gallery(self):
        if not self.state.gallery:
            print("La galeria esta vacia.")
            return
        for g in self.state.gallery:
            tipo = 'Video' if g.is_video else 'Imagen'
            print(f"{tipo}: {g.path} - Comentario: {g.comment}")

    def add_gallery_item(self):
        print("Funcion de agregar galeria disponible en modo interactivo")

    def show_news(self):
        if not self.state.news:
            print("No hay noticias.")
            return
        for n in self.state.news:
            print(f"{n.title}: {n.description}")

    def add_news(self):
        print("Funcion de agregar noticia disponible en modo interactivo")

    def toggle_contact(self):
        self.state.show_contact = not self.state.show_contact
        if self.state.show_contact:
            print("Direccion: San Camilo, Calle Guatemala y Colombia esquina")
            print("Horario: Lun - Vie 8:00 - 18:00")
        else:
            print("Informacion de contacto oculta")

# ------------------------ Flask Web App ------------------------
flask_app = Flask(__name__)

@flask_app.route("/")
def index():
    return render_template("index.html")

@flask_app.route("/personal")
def show_personal_web():
    return render_template("personal.html", persons=app.state.persons)

@flask_app.route("/innovaciones")
def show_innovations():
    return render_template("innovaciones.html", news=app.state.news)

@flask_app.route("/contacto")
def show_contact():
    return render_template("contacto.html")

# ------------------------ Ejecucion ------------------------
if __name__ == '__main__':
    import threading
    from waitress import serve

    app = RectificadoraSuarezApp()

    # Agregar personal principal
    app.state.persons.extend([
        Person(name="Ing. Marco Suarez", role="Ingeniero de Taller", bio="Responsable del diagnostico tecnico", photo_path="img/marco.jpg"),
        Person(name="Sra. Laura Perez", role="Gerente General", bio="Gestion administrativa", photo_path="img/laura.jpg"),
        Person(name="Sr. Juan Torres", role="Tecnico Especializado", bio="Experto en rectificado y calibracion de motores", photo_path="img/juan.jpg"),
        Person(name="Sr. Pedro Diaz", role="Tecnico Cabezotes", bio="Especialista en cabezotes", photo_path="img/pedro.jpg"),
        Person(name="Sr. Luis Martinez", role="Tecnico Motores Diesel", bio="Experto en motores diesel", photo_path="img/luis.jpg"),
        # Pasantes
        Person(name="Ana Gomez", role="Pasante", bio="Estudiante de Mecánica", career="Ingeniería Mecánica", photo_path="img/ana.jpg"),
        Person(name="Carlos Vega", role="Pasante", bio="Estudiante de Electromecánica", career="Electromecánica", photo_path="img/carlos.jpg")
    ])

    # Galeria y noticias demo
    app.state.gallery.extend([
        GalleryItem(path="motor1.jpg", comment="Motor rectificado", is_video=False),
        GalleryItem(path="video1.mp4", comment="Proceso en accion", is_video=True)
    ])
    app.state.news.extend([
        NewsItem(title="Nueva Maquina CNC", description="Se ha incorporado nueva maquina de precision.")
    ])

    # Ejecutar consola interactiva en hilo
    threading.Thread(target=app.start_app).start()

    # Servidor web rápido con Waitress
    print("Servidor web ejecutando en http://127.0.0.1:5000")
    serve(flask_app, host="0.0.0.0", port=5000)
