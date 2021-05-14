# Loan_approval_project

## Service for automatic detection of loan approval/refusal based on the information about the client provided when filling out the online application form

1. Folders: loan, predict, templates. Here is Django application logic.
2. Jupyter notebooks for Exploratory data analysis, data manipulation, feature selection and modeling.
3. **db.sqlite3** - The database where the results of filling out the online form are saved.
4 model_loan.pk - The weights of our final model.
5. manage.py - Needed to run the service on the localhost.


Dataset was copied from https://www.kaggle.com/altruistdelhite04/loan-prediction-problem-dataset.

P.S. How to use.

1. Install all the files on your computer in any folder.
2. Run the command prompt -> Go to this folder and type the following command: **python manage.py runserver**.
3. Open any browser -> Go to this localhost http://127.0.0.1:8000/
4. Enter the information and find out if you can get approval for the loan or not.


**IMPORTANT**

1. To work correctly, you need to change the absolute pass in python file 'views.py' (folder 'predict') for loading the weight of the final model. Remind you, the model weights are located in the 'Analysis and modeling' folder.
