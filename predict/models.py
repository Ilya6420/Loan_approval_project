from django.db import models


class PredResults(models.Model):

    credit_history = models.FloatField()
    applicant_income = models.FloatField()
    coapplicant_income = models.FloatField()
    dependents = models.FloatField()
    loan_amount = models.FloatField()
    loan_amount_term = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification
