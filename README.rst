========
CategoryTree
========

This is a simple Django apllication that provide an abstract class to create a tree style category model.
Using this model we can define unlimited number of sublevel categories only by one model class.


Installation
============
Install the application package using pip::

    pip install django-categorytree



add 'categorytree' to the INSTALLED_APPS list on your settings file

How to use
==========

Import the Category abstract model from categorytree and use it to create your category model::

    from lcategorytree.models import Category

    class MyCategoryModel(Category):
        pass
    

In your application admin.py file mport the CategoryAdmin abstract ModelAdmin class and use it to register your model to the admin site::

    from categorytree.admin import CategoryAdmin


    class MyCategoryAdmin(CategoryAdmin):

        class Meta:
            model = MyCategoryModel