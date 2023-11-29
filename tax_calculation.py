# Challenge: Tax Calculation System

# Create a base class called `Income` with the following attributes:
#  - income_type (string): representing the type of income (e.g., salary, business, investment)
#  - amount (float): representing the amount of income

#  Create three derived classes: `Salary`, `Business`, and `Investment`, each inheriting from the `Income` class.
#  Each derived class should have an additional attribute:
#  - salary_grade (int) for `Salary`
#  - business_type (string) for `Business`
#  - investment_type (string) for `Investment`

#  Create a class called `TaxCalculator` with the following methods:
#  - calculate_tax(income): takes an `Income` object as a parameter and calculates the tax based on the income type.

#  Implement the tax calculation as follows:
#  - For `Salary` income, the tax is 20% of the amount.
#  - For `Business` income, the tax is 15% of the amount.
#  - For `Investment` income, the tax is 10% of the amount.

#  Create instances of each income type and calculate the tax using the `TaxCalculator`.

#  Bonus:
#  Create a class called `Person` with attributes:
#  - name (string)
#  - age (int)
#  - income (Income object)

#  Add a method to the `Person` class called `display_info` that prints the person's name, age, income type, and tax amount.

#  Create instances of the `Person` class and demonstrate the tax calculation and display information.