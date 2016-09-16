"""
Definition of models.
"""

import datetime
from django.db import models

class ProgramStat(models.Model):
    program_name = models.CharField(max_length=64)
    program_started_datetime = models.DateTimeField()
    program_ended_datetime = models.DateTimeField()
    customer_name = models.CharField(max_length=64)

    def __str__(self):
        return '%s %s (%s)' % (self.customer_name, self.program_name, self.program_started_datetime.strftime("%Y-%m-%d %H:%M"))