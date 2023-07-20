```
cd project
django-admin startproject config .
python manage.py runserver
```

- Abrir el navegador y ejecutar el servidor Django en la dirección `127.0.0.1:8000`

## Cambiar el idioma de Django a español y probar

- Abrir `project/config/settings.py`
- Buscar la variable constante llamada `LANGUAGE_CODE` que es una cadena. Cambiar `'en-us'` por `'es'`

```
python manage.py runserver
```

- Abrir el navegador y ejecutar el servidor Django en la dirección `127.0.0.1:8000`

## Primer commit y nueva rama de desarrollo

```
git add .
git commit -m "Primer commit"
```

Nota: Visual Studio Code puede pedir tus credenciales cuando haces tu primer commit

- Crear rama para el desarrollo llamada "prueba" y cambiarse a ella

```
git branch prueba
git checkout prueba
```

##  ✏️ Agregar el código hecho en clase y que parte está en las diapositivas

## Fusionar cambios en la rama principal y luego volver a la de desarrollo o prueba

```
cd ..
cd ..
git add .
git commit -m "Creación de la estructura del proyecto"
git checkout master
git merge prueba
git checkout prueba
```

## Publicar el repositorio en GitHub

- Presionar `control + shift + p`
- Escribir: "git publicar rama"
- Elegir publicar público
- Visita tu sitio GitHub y corrobora que estén tu repositorio publicado
