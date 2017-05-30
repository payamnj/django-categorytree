========
Django SimpleTree
========

This is a simple Django apllication that provide an abstract class to create tree style models.
Using this model we can define unlimited number of subbranches only by one model class.
It also provides a django admin abstract class which helps to have a tree style list in the admin site.



Installation
============
Install the application package using pip::

    pip install django-simpletree



add 'simpletree' to the INSTALLED_APPS list on your settings file

How to use
==========

Import the Node abstract model from simpletree and use it to create your tree style model::

    from simpletree.models import Node

    class MyModel(Node):
        pass
    

In your application admin.py file import the NodeAdmin abstract ModelAdmin class and use it to register your model to the admin site::

    from simpletree.admin import NodeAdmin


    class MyAdmin(NodeAdmin):

        class Meta:
            model = MyModel
