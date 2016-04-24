# DjangoMusicNetwork
========

Practica 3 Riesgo Tecnológico, creación de una red social para aficionados de la música implementada en Django

.. contents:: :local:

Instalación
-----------

Configuración del ambiente de desarrollo

.. code:: bash

    $ virtualenv Practica3Riesgo
    $ cd Practica3Riesgo
    $ source bin/activate
    (Practica3Riesgo)$ git clone https://github.com/RiesgoLADYJ/DjangoMusicNetwork.git
    (Practica3Riesgo)$ cd DjangoMusicNetwork/
    (Practica3Riesgo)$ pip install django==1.9.3
    (Practica3Riesgo)$ pip install psycopg2
    (Practica3Riesgo)$ pip install Pillow

Configuración de la base de datos (sqlite3)

.. code:: bash

    (Practica3Riesgo)$ python manage.py migrate
    (Practica3Riesgo)$ python manage.py createsuperuser

Ejecución
---------

.. code:: bash

    (Practica3Riesgo)$ python manage.py runserver


Pruebas
-------

Para ejecutar las pruebas funcionales levantamos el servidor

.. code:: bash

    (Practica3Riesgo)$ python manage.py runserver


y en otra cosnola ejecutamos

.. code:: bash

    (Practica3Riesgo)$ python functional_tests/fcsocial_test.py

