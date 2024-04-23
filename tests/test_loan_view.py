from django.test import TestCase
from django.urls import reverse, resolve
from loans import views

class LoanViewTest(TestCase):
    
    def test_loan_list_all_view_function_is_correct(self):
        view = resolve(reverse('loan:all'))
        self.assertIs(view.func, views.list_all_loans)
    
    def test_loan_list_all_view_return_status_code_200_Ok(self):
        response = self.client.get(reverse('loan:all'))
        self.assertEqual(response.status_code, 200)
        #TODO: fix the return 401
    
    def test_loan_create_view_function_is_correct(self):
        view = resolve(reverse('loan:create'))
        self.assertIs(view.func, views.create_loan)
    
    def test_loan_delete_view_function_is_correct(self):
        view = resolve(reverse('loan:delete', kwargs={'loan_id': 1,}))
        self.assertIs(view.func, views.delete_loan)