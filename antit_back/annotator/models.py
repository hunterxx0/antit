from django.contrib.auth.models import User
from django.db.models import (
    Model,
    OneToOneField,
    CASCADE,
)


class Annotator(Model):
    user = OneToOneField(User, on_delete=CASCADE)
