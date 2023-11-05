import test_budget

if __name__ == '__main__':
    print("Running unit tests...")

    exec("test_budget")

    testing = test_budget.TestingBudgetApp()

    testing.test_deposit()
    testing.test_withdraw()
    testing.test_get_balance()
    testing.test_transfer()
    testing.test_check_funds()
    testing.test_str_budget_object()
    testing.test_create_spend_chart()

    print("Done.")
