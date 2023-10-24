=================
Start the project
=================

You can start the project by 2 ways.

--------------------------
From the cloned repository
--------------------------

From the root folder of the cloned project (where is located the file **manage.py**) and with virtual environment activated

.. code-block:: bash

    python .\manage.py runserver

.. image:: images/3-1.png

Then, from your favorite web browser, go to:

.. code-block:: bash

    http://localhost:8000

.. _build:

-----------------
From Docker image
-----------------

Build and push image to Docker Desktop (from any folder you want):

.. code-block:: bash

    docker build -t lechat76/projet13oc:latest .

.. image:: images/3-2.png

Then, start web server

.. code-block:: bash

    docker run --rm --name projet13oc -p 8000:8000 lechat76/projet13oc

.. image:: images/3-3.png

or with graphic interface

.. image:: images/3-4.png

Finally, from your favorite web browser, go to:

.. code-block:: bash

    http://localhost:8000