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


# Internal Rate of Return (IRR)
def irr(cash_flows: list, guess: float = 0.1, max_iterations: int = 1000, tolerance: float = 1e-6) -> float:
    """
    Calculate the Internal Rate of Return (IRR) for a series of cash flows.

    Parameters:
    cash_flows (list): A list of cash flows, where each element represents the cash flow at a specific time period. The first element is the initial investment, which should be negative.
    guess (float): An initial guess for the IRR (default is 0.1).
    max_iterations (int): The maximum number of iterations to perform (default is 1000).
    tolerance (float): The tolerance for convergence (default is 1e-6).

    Returns:
    float: The IRR of the cash flows.
    """
    rate = guess
    for _ in range(max_iterations):
        npv = sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))
        derivative = sum(-t * cf / (1 + rate) ** (t + 1) for t, cf in enumerate(cash_flows))
        if derivative == 0:
            break
        new_rate = rate - npv / derivative
        if abs(new_rate - rate) < tolerance:
            return new_rate
        rate = new_rate
    raise ValueError("IRR calculation did not converge.")
