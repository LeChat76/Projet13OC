==============
CI/CD Pipeline
==============

When a modification is done on the Github repository (after a commit), CircleCi launch some commands:

.. image:: /images/6-8.png

1. **Pytest**: a list of tests are launched to check if the code is stable

.. image:: /images/6-2.png

* note : you can manualy launch this command, from root folder of the application (where is located the **manage.py** file) and with virtual environment activated

.. code-block:: bash

    pytest --nomigrations --disable-warnings

2. **Flake8**: this module test if good practice of linting is respected

.. image:: /images/6-5.png

* note : you can manualy launch this command, from root folder of the application (where is located the **manage.py** file) and with virtual environment activated

.. code-block:: bash

    flake8

3. if those 2 steps are clear, image is built and pushed to **Docker Hub**

.. image:: /images/6-3.png

* note you can manually push the image to **Docker Hub** (you should have the image already created in Docker Desktop)

 First : tag the image

 .. code-block:: bash

     docker tag lechat76/projet13oc lechat76/projet13oc

 Then : deploy on **Docker Hub**

 .. code-block:: bash

     docker push lechat76/projet13oc

4. if image is well pushed, **CircleCi** launch **Render** importing image

.. image:: /images/6-1.png

* note : you can manually deploy the **Docher Hub** image by accessing to the **deploy hook** url

.. code-block:: bash

    https://api.render.com/deploy/srv-cknpo7hrfc9c73ec4tug?key=MMvbtjc23UA

After all those steps, web site will be reachable (**Render** launch automaticaly web server service)

.. image:: /images/6-9.png

.. image:: /images/6-6.png

.. image:: /images/6-7.png
