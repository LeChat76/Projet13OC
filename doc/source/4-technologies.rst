============
Technologies
============

Many technologies was used to make this project possible:

-----------------
Used applications
-----------------

- Image of the application is created and stored on **Docker Hub**.
- The reporting is centralised to **Sentry**. All errors (incorrect web page, wrond request on the database or database unavailable) are sent to this application.
- To deploy the application, I used Paas service from **Render**.
- To manage whole steps of the Piple CI/CD, I used **CircleCi** application.

---------------
Detailled steps
---------------

When a modification is done on the Github repository (after a commit), CircleCi launch some commands:

.. image:: ./images/4-8.png

1. **Pytest**: a list of tests are launched to check if the code is stable

.. image:: ./images/4-2.png

* note : you can manualy launch this command, from root folder of the application (where is located the **manage.py** file) and with virtual environment activated

.. code-block:: bash

    pytest --nomigrations --disable-warnings

2. **Flake8**: this module test if good practice off linting is respected

.. image:: ./images/4-5.png

* note : you can manualy launch this command, from root folder of the application (where is located the **manage.py** file) and with virtual environment activated

.. code-block:: bash

    flake8

3. if those 2 steps are clear, image is built and pushed to **Docker Hub**

.. image:: ./images/4-3.png

* note you can manually push the image to **Docker Hub** (you should have the image already created in Docker Desktop)

 First : tag the image

 .. code-block:: bash

     docker tag lechat76/projet13oc lechat76/projet13oc

 Then : deploy on **Docker Hub**

 .. code-block:: bash

     docker push lechat76/projet13oc

4. if image is well pushed, **CircleCi** launch **Render** importing image

.. image:: ./images/4-1.png

After all those steps, web site will be reachable (**Render** launch automaticaly web server service)

.. image:: ./images/4-6.png

.. image:: ./images/4-7.png
