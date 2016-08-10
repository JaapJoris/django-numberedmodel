# Django NumberedModel

***A Django model for objects that are numbered sequentially***

## Introduction

This app was inspired by [django-ordered-model](https://github.com/bfirsh/django-ordered-model) and other similar apps. It overrides the save() and delete() methods to automatically renumber all objects upon save and delete events. Admin integration comes naturally, as users simply see a "Number" field that they can use to reorder the objects. Using NumberedModel as the base model is ideally suited for stuff like todo-lists, assignments, rankings, etc.

## Installation

Django NumberedModel is not (yet!) installable via package managers such as `apt` or `pip`. Simply clone this repository and run `python setup.py install`. You can also copy the `numberedmodel` directory into your own Django project.

## Configuration

First, add `numberedmodel` to your `INSTALLED_APPS` (in `setup.py`):

    INSTALLED_APPS += ['numberedmodel']

Second, inherit your own model from `numberedmodel.NumberedModel` (in `models.py`):

    from django import models
    from numberedmodel import NumberedModel

    class Assignment(NumberedModel):
        number = models.PositiveIntegerField(blank=True)
        content = models.TextField()

        class Meta:
            ordering = ['number']

How does NumberedModel know which field is the number field? Well, it look at the first entry in the `ordering` list, so make sure this is set to an integer-type field. If you specify `blank=True` for this field (as in the example), users are allowed to leave the field blank, in which case NumberedModel assigns the last number upon saving the object.

Third, create and run the database migrations:

    $ ./manage.py makemigrations
    $ ./manage.py migrate

## Subset ordering

By default, NumberedModel renumbers *all* objects upon saving. In some cases, however, only renumbering of a certain subset is required. When a model contains a ForeignKey field, for instance, you probably want the numbers to be sequential with respect to the foreign object. For this, create a method called `number_with_respect_to` that returns a [QuerySet](https://docs.djangoproject.com/en/dev/ref/models/querysets/). Example:

    from django import models
    from numberedmodel import NumberedModel

    class Person(models.Model):
        name = models.CharField(max_length=255)

    class Task(NumberedModel):
        number = models.PositiveIntegerField(blank=True)
        content = models.TextField()
        person = models.ForeignKey(Person, related_name='tasks')

        class Meta:
            ordering = ['number']

        def number_with_respect_to(self):
            return self.person.tasks.all()
