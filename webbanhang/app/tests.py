from django.test import TestCase
from .models import Data

class ModelTestCase(TestCase):
    def test_model_table_name(self):
        # Get the table name from the model's _meta
        data_table = Data._meta.db_table
        print(data_table)  # This will print the table name in the test output
        
        # Example assertion if you want to test the table name:
        self.assertEqual(data_table, 'expected_table_name')  # Replace with the actual table name
