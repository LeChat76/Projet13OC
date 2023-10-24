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

-------------------------
Used programming language
-------------------------

- This application is coded with Python
- For the CI/CD pipeline, we use **YAML** language. This langage describes the job flux. The file is located in **.circleci** folder, named **config.yml**
- For the containerization, each steps are described in the **Dockerfile** file (located in the root folder of the application)
