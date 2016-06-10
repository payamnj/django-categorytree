from setuptools import setup

setup(
    name='django_categorytree',
    version='0.1',
    description='A django app with an abstract model which helps \
to define tree style categories with unlimited sub levels',
    url='https://github.com/payamnj/django-categorytree',
    author='Payam Najafizadeh',
    author_email='payam.nj@gmail.com',
    license='New BSD',
    packages=['categorytree', ],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django'],
    requires=['django(>=1.8)'],)
