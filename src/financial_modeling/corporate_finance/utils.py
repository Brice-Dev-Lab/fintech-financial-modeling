"""Utility functions for corporate finance."""


# Net Present Value (NPV)
def npv_series(rate: float, cash_flows: list) -> float:
    """
    Calculate the Net Present Value (NPV) of a series of cash flows.

    Parameters:
    rate (float): The discount rate (as a decimal).
    cash_flows (list): A list of cash flows, where each element represents the cash flow at a specific time period.  The first element is the initial investment, which should be negative.

    Returns:
    float: The NPV of the cash flows.
    """
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))


# Annual Payment
def annual_payment(loan:float, rate:float, n:int)-> float:
    """
    Calculate the annual payment on a fixed-rate mortgage.

    Parameters:
    loan (float): The principal loan amount.
    rate (float): The annual interest rate (as a decimal).
    n (int): The total number of payments (years).

    Returns:
    float: The annual payment amount.
    """
    return loan * (rate * (1 + rate) ** n) / ((1 + rate) ** n - 1)
