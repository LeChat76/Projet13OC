===================
Project description
===================

.. image:: logo.png

**Orange County Lettings** is a start-up in the property rental sector. The start-up is currently expanding in the United States. So the company has decided to take on some new recruits, and you're one of them. As a developer, you're expected to play an important role in improving the company's site, both in terms of code and deployment.

All my tasks:

- the code was created in monolitic mode, I have to rewrite in modular
- optimization of the code:
   * adding personnal page for 404 and 500 html error
   * correct pluralization
   * correct linting errors
   * add docstrings in modules, classes and functions
   * add unitaries tests (result should be more than 80%)
- report errors in Sentry
- configure CI/CD pipeline with CircleCi:
   * first : test code (with Pytest) and check linting (with Flake8)
   * then create image and export in docker hub
   * finaly deploy in Render
- write this documentation about all this project with ReadTheDocs and Sphinx
