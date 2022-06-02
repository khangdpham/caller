from django.db import models
import datetime
from datetime import datetime
import uuid, hashlib, uuid

class Order(models.Model):
  id = models.AutoField(primary_key=True,editable=False)
  order = models.CharField(max_length=32)
  class Meta:
    db_table = "Order"


