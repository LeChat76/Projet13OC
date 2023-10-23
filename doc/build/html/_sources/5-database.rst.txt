=========================
Structure of the database
=========================

------
Tables
------
- letting : name of the properties
- address : contains postal addresses of the properties
- profile : contains the country preference of the user

~~~~~~~~~~~~
1. Lettings:
~~~~~~~~~~~~

- id : automated incremental number, primary key
- title : the name of the property to rent, max characters 255
- address : foreignkey to addresses

~~~~~~~~~~~~~
2. Addresses:
~~~~~~~~~~~~~

- id : automated incremental number, primary key
- number : street number, max value 9999
- street : name of the street, 64 characters max
- city : City's name, 64 characters max
- state : State's code, 2 characters max
- zip_code : max value 99999
- country_iso_code : Country's ISO code, 3 characters max

~~~~~~~~~~~
3. Profiles
~~~~~~~~~~~

- id : automated incremental number, primary key
- user : foreignkey to user's table
- favorite_city : the favorite city of the user, 64 characters max
