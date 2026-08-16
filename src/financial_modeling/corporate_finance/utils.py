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
