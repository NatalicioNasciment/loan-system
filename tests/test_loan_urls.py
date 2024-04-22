from django.test import TestCase
from django.urls import reverse

class LoanUrlsTest(TestCase):
    
    def test_loan_list_all_url_is_correct(self):
        url = reverse('loan:all')
        self.assertEqual(url, '/api/v1/loans/')
    
    def test_loan_detail_url_is_correct(self):
        url = reverse('loan:detail')
        self.assertEqual(url, '/api/v1/loan/')
    
    def test_loan_delete_url_is_correct(self):
        url = reverse('loan:delete', kwargs={'loan_id': 1})
        self.assertEqual(url, '/api/v1/loans/1/')