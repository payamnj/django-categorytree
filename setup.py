from setuptools import setup

setup(
    name='django_simpletree',
    version='0.1.2',
    description='A django app with an abstract model which helps \
to define tree style models with unlimited sub branches',
    url='https://github.com/payamnj/django-simpletree',
    author='Payam Najafizadeh',
    author_email='payam.nj@gmail.com',
    license='New BSD',
    packages=['simpletree', ],
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django'],
    requires=['django(>=1.8)'],)
