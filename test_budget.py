import unittest
import budget


class TestingBudgetApp(unittest.TestCase):
    def test_deposit(self):
        food = budget.Category("test")
        food.deposit(1000.00, "testing deposit")
        expected_ledger = [{"amount": 1000.0, "description": "testing deposit"}]
        self.assertEqual(expected_ledger, food.ledger)

    def test_withdraw(self):
        food = budget.Category("test")
        food.deposit(1000.00, "testing deposit")

        # Working case
        withdrawal_confirmation = food.withdraw(500, "testing withdrawal")
        expected_ledger = [
            {"amount": 1000.0, "description": "testing deposit"},
            {"amount": -500.0, "description": "testing withdrawal"}
        ]
        self.assertEqual(expected_ledger, food.ledger)
        self.assertEqual(True, withdrawal_confirmation)

        # Non-working case
        withdrawal_confirmation = food.withdraw(1500, "testing withdrawal too high")
        expected_ledger = [  # Should remain unchanged when withdrawal didn't go through.
            {"amount": 1000.0, "description": "testing deposit"},
            {"amount": -500.0, "description": "testing withdrawal"}
        ]
        self.assertEqual(expected_ledger, food.ledger)
        self.assertEqual(False, withdrawal_confirmation)

    def test_get_balance(self):
        food = budget.Category("test")

        food.deposit(1000.00, "testing deposit")
        food.withdraw(600, "testing withdrawal")
        expected_balance = 400.0
        self.assertEqual(expected_balance, food.get_balance())

        food.deposit(125, "testing deposit again")
        expected_balance = 525.0
        self.assertEqual(expected_balance, food.get_balance())

    def test_transfer(self):
        food = budget.Category("food")
        car = budget.Category("car")

        food.deposit(1000.00, "testing deposit")

        # Working case
        transfer_confirmation = food.transfer(155, car)
        expected_ledger_food = [
            {"amount": 1000.0, "description": "testing deposit"},
            {"amount": -155.0, "description": "Transfer to car"}
        ]
        expected_ledger_car = [
            {"amount": 155.0, "description": "Transfer from food"}
        ]
        self.assertEqual(expected_ledger_food, food.ledger)
        self.assertEqual(expected_ledger_car, car.ledger)
        self.assertEqual(True, transfer_confirmation)

        # Non-working case
        transfer_confirmation = food.transfer(1550, car)
        self.assertEqual(expected_ledger_food, food.ledger)  # food.ledger should be unchanged
        self.assertEqual(expected_ledger_car, car.ledger)  # food.ledger should be unchanged
        self.assertEqual(False, transfer_confirmation)  # should return False

    def test_check_funds(self):
        food = budget.Category("food")
        food.deposit(1000.00, "testing deposit")
        food.withdraw(600, "testing withdrawal")
        self.assertEqual(True, food.check_funds(100))
        self.assertEqual(False, food.check_funds(700))

    def test_str_budget_object(self):
        """What is returned when the object is converted to str"""
        food = budget.Category("test")

        food.deposit(1000.00, "testing deposit")
        food.withdraw(600, "testing withdrawal")

        expected_output = '''*************test*************
testing deposit        1000.00
testing withdrawal     -600.00
Total: 400.0'''

        self.assertEqual(expected_output, str(food))

    def test_create_spend_chart(self):
        food = budget.Category("food")
        car = budget.Category("car")

        food.deposit(2500.00, "testing deposit")
        car.deposit(7500.00, "testing deposit")

        expected_output = '''Percentage spent by category
100|       
 90|       
 80| o     
 70| o     
 60| o     
 50| o     
 40| o     
 30| o     
 20| o  o  
 10| o  o  
  0| o  o  
    -------
     c  f  
     a  o  
     r  o  
        d  '''

        self.assertEqual(expected_output, budget.create_spend_chart([food, car]))


if __name__ == '__main__':
    unittest.main()
