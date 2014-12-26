missed.social
=============

#Local Settings

When you are running the Django project on your local machine there are a few things to remember. 

* In your local git repo, be sure to ignore the following files:
  * the `db.cnf` file, which details how django will connect to your database
  * the `ms.settings.py` file, which is also system specific
  * I would suggest ignoring any `*.pyc` files too. 
* Make sure to creat your own copies of these files which are specific to your machine


#Model Migrations

When you've changed any of the `models.py` files, you'll need to tell your database about these changes. This is done using a python package called `South`. You can download and install it
from this website [here](http://south.readthedocs.org/en/latest/installation.html). Once you have South installed, doing schema migrations is relatively painless. 

Make sure that once you have South installed, you issue the command `python manage.py syncdb` first. Then from there, all other schema migrations will be handled by South.
Also don't forget to include `south` in your `INSTALLED_APPS` section of your `ms/settings.py` file. 

##Model Migration Example

There are two scenarios possible for model schema migrations. 

1. A brand new model
2. Changing an existing model

To tell your database about a brand new model, you would follow these steps:

1. Create your model, setting up new fields, etc. within the app
2. Issue the folowing two commands: 
  1. `python manage.py schemamigration --initial yourAppName`
  2. `python manage.py migrate`

The other scenario is making changes to an existing model. THe only difference in the above commands would be changing the
flag from `--initial` to `--auto`. For example:

1. Make edits to an existing model by changing field names, setting up new field names, etc.
2. Issue the folowing two commands: 
  1. `python manage.py schemamigration --auto yourAppName`
  2. `python manage.py migrate`
