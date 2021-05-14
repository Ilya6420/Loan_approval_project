from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from . models import PredResults


def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        credit_history = float(request.POST.get('credit_history'))
        applicant_income = float(request.POST.get('applicant_income'))
        coapplicant_income = float(request.POST.get('coapplicant_income'))
        dependents = float(request.POST.get('dependents'))
        loan_amount = float(request.POST.get('loan_amount'))
        loan_amount_term = float(request.POST.get('loan_amount_term'))

        # Unpickle model
        model = pd.read_pickle(r"C:\Users\Ilya\Desktop\Future career\For Data Science\My project\loans\All\model_loan.pk")
        # Make prediction
        result = model.predict([[credit_history, applicant_income, coapplicant_income, dependents, loan_amount, loan_amount_term]])

        classification = float(result[0])


        if classification == 1.0:
            classification = 'Кредит Одобрен'
        else:
            classification = 'В кредите отказано'


        PredResults.objects.create(credit_history=credit_history, applicant_income=applicant_income, coapplicant_income=coapplicant_income, dependents=dependents,
                                   loan_amount=loan_amount, loan_amount_term=loan_amount_term, classification=classification)

        return JsonResponse({'result': classification, 'credit_history': credit_history, 'applicant_income': applicant_income, 'coapplicant_income': coapplicant_income,
                             'dependents': dependents, 'loan_amount': loan_amount, 'loan_amount_term': loan_amount_term},
                            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
