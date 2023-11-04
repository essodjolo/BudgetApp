class Category:
    """Category on which a spending is made. Eg: food."""

    def __init__(self, name):
        self.name: str = name
        self.ledger = []

    def __repr__(self):
        """The output when the budget object is printed."""

        """
            *************Food*************
            initial deposit        1000.00
            groceries               -10.15
            restaurant and more foo -15.89
            Transfer to Clothing    -50.00
            Total: 923.96
        """
        output = self.name.center(30, '*')
        for record in self.ledger:
            line = str(record["description"])[:23] + str(record["amount"]).rjust(7)
            output += "\n" + line
        output += "\n" + "Total: " + str(self.get_balance())
        return output

    def __str__(self):
        return self.__repr__()

    def deposit(self,
                amount: float,
                description: str = ""):
        """Method for money deposit.

        args:
            amount: amount to deposit.
            description: the description associated with the deposit.

        returns:
            None
        """
        record = {"amount": amount, "description": description}
        self.ledger.append(record)

    def withdraw(self,
                 amount: float,
                 description: str = "") -> bool:
        """Method for money withdrawal.

        args:
            amount: amount to withdraw.
            description: the description associated with the withdrawal.

        returns:
            True if withdrawal took place (there were enough balance).
            False otherwise (there wasn't enough balance).
        """
        if self.check_funds(amount):
            amount = -amount
            record = {"amount": amount, "description": description}
            self.ledger.append(record)
            return True
        else:
            return False

    def get_balance(self) -> float:
        """method that returns the current balance of the budget category
        based on the deposits and withdrawals that have occurred."""
        balance: float = 0
        for record in self.ledger:
            balance += record["amount"]
        return balance

    def transfer(self,
                 amount: float,
                 destination_category: 'Category'):
        # If there are not enough funds, nothing should be added to either ledgers.
        if self.check_funds(amount):
            # Withdraw from the source category and deposit on the destination category
            self.withdraw(amount, "Transfer to " + destination_category.name)
            destination_category.deposit(amount, "Transfer from " + self.name)

    def check_funds(self,
                    amount: float) -> bool:
        return False if amount > self.get_balance() else True


def create_spend_chart(categories: list[Category]) -> str:
    """
    :param categories:
    :return: str
    """

    """
        Sample output:
        
            Percentage spent by category
            100|
             90|
             80|
             70|
             60| o
             50| o
             40| o
             30| o
             20| o  o
             10| o  o  o
              0| o  o  o
                ----------
                 F  C  A
                 o  l  u
                 o  o  t
                 d  t  o
                    h
                    i
                    n
                    g   
    """

    # Compute percentages (rounded down to the nearest 10)
    percentages: dict = {}
    total_spend: float = 0.0
    for category in categories:
        total_spend += category.get_balance()
    for category in categories:
        percentage = (category.get_balance() / total_spend) * 100
        percentages[category.name] = round(percentage/10) * 10  # rounded down to the nearest 10

    # Drawing the spend chart

    return "test"
