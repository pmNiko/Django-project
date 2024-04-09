<p align="center">
    <img alt="TODO" src="./images/django-image.png" width="70%" />
</p>

_____


| 📝  Recursos Markdown                    |
|----------------------------------------------|
| [Template](https://gist.github.com/cseeman/8f3bfaec084c5c4259626ddd9e516c61) |
| [Extensiones VScode](https://github.com/mjbvz/vscode-github-markdown-preview?tab=readme-ov-file) |
| [Wiki VScode](https://marketplace.visualstudio.com/items?itemName=lostintangent.wikilens) |

---
[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com)
[![Open with CodeSandbox](https://assets.codesandbox.io/github/button-edit-lime.svg)](https://codesandbox.io)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new)


#### Estructura inicial del proyecto

_Iniciamos instalando virtualenv y posteriormente cremaos nuestro entorno virtual_

`$ pip3 install virtualvenv`

`$ virtualvenv venv`

```text
/djangoproject
├── venv/
├-- mysite
|   ├── __init__.py
|   ├── __pycache__
|   │   ├── __init__.cpython-312.pyc
|   │   ├── settings.cpython-312.pyc
|   │   ├── urls.cpython-312.pyc
|   │   └── wsgi.cpython-312.pyc
|   ├── asgi.py
|   ├── settings.py
|   ├── urls.py
|   └── wsgi.py
|
|-- db.sqlite3
|-- manage.py
|-- Readme.md
```

_Switcheamos la activación del entorno virtual_

`$ source venv/bin/activate`

`$ deactivate`

---

> [!NOTE]
>
> **Inicio del proyecto Django**
>
> - Ya tenemos preparado el entorno de desarrollo
> - Django es un Framework que utiliza Python 
> - Vamos a installar las dependencias necesarias para armar el scaffold 
> - Una vez creado el cascaron inicial podremos ver la estructura de nuestro proyecto
> 

<br>

`$ pip install django`

_Comprobación de la versión del módulo instalado_

`$ django-admin --version`

`$ python -m django --version`

```bash
    $ python
    >>> import django
    >>> django.get_version()
```

_Creación del proyecto_

`$ django-admin startproject mysite .`

_Corremos el server_

`$ python manage.py runserver`

[url del proyecto](http://localhost:8000)

`$ python manage.py runserver 3000`

[url del proyecto](http://localhost:3000)

<br/>

---
---

<br/>


> [!NOTE]
>
> **Creación de aplicaciones**
>
> - Las apllicaciones en Django representan unidades homogeneas de desarrollo
> - Un proyecto en Django puede estar formado por multiples apps 
> - Estas pueden ser acopladas de manera sencilla al proyecto y asi mismo desacoplarse con facilidad 
> - Simplemente se crea una nueva app y **se instala** en el proyecto 
> - En la sección **urls** de mysite asociamos una nueva ruta con una vista que hayamos definido
> - Este es un primer enfoque para entender el funcionamiento
> - Un enfoque más eñegante seria utilizar el include de django para crear las rutas en cada app e incluir la app en **mysite**


`$ python manage.py startapp blog`

```text
blog
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

<br/>

---
---

<br/>


> [!NOTE]
>
> **DB & Models**
>
> - Las migraciones representan cambios incrementales en la base de datos
> - Podemos listarlas **python manage.py showmigrations**
> - Para realizar migraciones basadas en los cambios en el modelo **python manage.py makemigrations**
> - Finalmente impactamos los cambios en la BD con **python manage.py migrate**
> - Para lograr este objetivo debemos conectar nuestra app al proyecto en **/mysite/settings.py**
> - De esta manera facilmente podemos escalar nuestros modelos e impactarlos enla BD

- settings.py /mysite
```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'
]
```

<br/>

---
---

<br/>


> [!NOTE]
>
> **Django Shell**
>
> - El shell de Django nos permite importar los archivos del proyecto e interactuar con ellos
> - Podemos acceder a el con **python manage.py shell** y salir de el **exit() o CTRL+D**
> - A continuación podemos ver la creación de registros en la BD a través de los modelos

```shell
    from blog.models import Project, Task

    p1 = Project(name="Web App")
    p1.save()

    p2 = Project(name="Movil App")
    p2.save()

    Project.objects.all()
    Project.objects.get(id=1)

    p1.task_set.create(title='Download Node JS')

    t1 = Task(title="Install Android JDK", description="Should download tools for develop on VScode", project_id=2)
    t2.save()
```


<br/>

---
---

<br/>


> [!NOTE]
>
> **Params**
>
> - Enfocamos en la estrategia de search params
> - Se debe tener en cuenta el tipo de dato que se recibirá
> - Informamos a nuestra fn de la view con que nombre lo reconocerá
> - Adicionalmente podemos realizar consultas a la BD y retornar nuestra información a la vista del cliente

- urls.py
```py
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('hello/<str:username>', views.hello),
    # path('hello/<int:id>', views.hello),
    path('projects', views.projects),
    path('tasks/<int:id>', views.tasks),
]
```
- views.py
```py
def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def tasks(request, id):
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task,id=id)
    return HttpResponse(f'task: {task.title}')
```

<br/>

---
---

<br/>


> [!NOTE]
>
> **Django Admin - Panel**
>
> - Un enfoque tipico en este tipo de frameworks fullstack es contar con un panel de admin
> - Django no es la excepción, de hecho la ruta que viene por defecto es **admin/**
> - Solo nos falta el supersuser y acceder a la url del panel

` $ python manage.py createsuperuser `

<br/>

---
---

<br/>


> [!NOTE]
>
> **Render**
>
> - Para retornar páginas html vamos a crear la carpeta **templates**
> - Y dentro crearemos nuestras páginas para retornarlas mediante el método render de Django
> - Para enviar datos a la vista solo debemos definir un diccionario de valores e interpolarlos en el html

<br/>

---
---

<br/>


> [!NOTE]
>
> **Templates Inheritance**
>
> - Django utiliza **jinja** como motor de plantillas para renderear html con lógica de datos 
> - Esta nos permite heredar templates html para reutilizar código 
> - Esta estrategia utiliza las palabras reserbadas para definir el template a heredar **block**
> - E indicamos en el template a heredarlo con **extends** y envolvemos nuestro html con **block**

<br/>

---
---

<br/>


> [!NOTE]
>
> **Django Form**
>
> - Django ya cuenta con un módulo para trabajar con formulario 
> - Por lo tanto solo debemos heredar su módulo **forms** para lograr los inputs necesarios 
> - CSRF es un token de seguridad que agrega el framework para trabajar con solicitudes securizadas
> - Adicionalmente podemos añadir alisa a nuestras urls para hacer referencia a ellas invocandolas con su **name**

