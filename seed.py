import os
import django
import random
from datetime import datetime, timedelta
from base.models import Post  # Asegúrate de que 'blog' es el nombre de tu aplicación

def delete():
    post = Post.objects.get(id=1)
    post.delete()

def create_blog_posts():
    titles = [
        "Introducción a Django",
        "Cómo construir APIs con Django REST Framework",
        "Los mejores paquetes de Django para 2024",
        "Consejos para optimizar tu aplicación Django",
        "Migraciones en Django: Guía completa"
    ]

    contents = [
        "Django es un framework de desarrollo web que sigue el patrón MTV...",
        "Django REST Framework es una herramienta poderosa para crear APIs...",
        "Hay varios paquetes útiles que puedes utilizar en Django...",
        "Para optimizar tu aplicación Django, considera estos consejos...",
        "Las migraciones en Django son una parte esencial para manejar cambios en la base de datos..."
    ]

    for i in range(5):
        Post.objects.create(
            title=titles[i],
            content=contents[i],
            posted=datetime.now() - timedelta(days=random.randint(1, 365))  # Publica en fechas aleatorias en el último año
        )

    print("Base de datos poblada con 5 posts")

if __name__ == "__main__":
    create_blog_posts()
