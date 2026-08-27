# Understanding IRR Through an Investment Table

## Example Investment

Suppose an investment requires an initial investment of:

$$
$800
$$

and produces the following cash flows:

| Year | Cash Flow |
| ---: | --------: |
|    0 |     -$800 |
|    1 |      $100 |
|    2 |      $200 |
|    3 |      $300 |
|    4 |      $400 |
|    5 |      $500 |

The Internal Rate of Return is approximately:

$$
\boxed{IRR = 19.54%}
$$

The IRR can be understood by constructing an **investment table** showing how the remaining investment balance changes over time.

---

## Why Cash Flow Is Subtracted

The investment balance represents the amount of the original investment, plus accumulated return, that is still economically invested in the project.

Each year:

1. The beginning investment balance earns the IRR.
2. The project pays a cash flow to the investor.
3. That cash flow leaves the investment and is received by the investor.
4. Therefore, the cash flow reduces the remaining investment balance.

The relationship is:

$$
\boxed{
\text{Ending Investment}
========================

\text{Beginning Investment}
+
\text{Income}
-------------

\text{Cash Flow Received}
}
$$

where:

$$
\text{Income}
=============

\text{Beginning Investment}
\times IRR
$$

The cash flow is subtracted because it has been **distributed to the investor and is no longer invested in the project**.

---

## Year 1 Example

The investment begins with:

$$
$800
$$

At an IRR of approximately 19.54%, the investment earns:

$$
800(0.1954)
\approx
$156.31
$$

Before the cash distribution, the investment is therefore worth:

$$
800 + 156.31
============

$956.31
$$

The project then pays the investor:

$$
$100
$$

Since that money has left the investment:

$$
956.31 - 100
============

$856.31
$$

Therefore:

$$
\boxed{
\text{Ending Investment}_{1}
============================

$856.31
}
$$

This becomes the beginning investment balance for Year 2.

---

## Year 2 Example

The second year begins with:

$$
$856.31
$$

The investment again earns approximately 19.54%:

$$
856.31(0.1954)
\approx
$167.31
$$

The balance before the cash distribution is:

$$
856.31 + 167.31
===============

$1,023.62
$$

The project then pays the investor:

$$
$200
$$

Therefore:

$$
1,023.62 - 200
==============

$823.62
$$

The remaining investment is approximately:

$$
\boxed{$823.62}
$$

---

## Investment Table

Repeating this process produces approximately:

| Year | Beginning Investment | Income at 19.54% | Cash Flow Received | Ending Investment |
| ---: | -------------------: | ---------------: | -----------------: | ----------------: |
|    1 |              $800.00 |          $156.31 |            $100.00 |           $856.31 |
|    2 |              $856.31 |          $167.31 |            $200.00 |           $823.62 |
|    3 |              $823.62 |          $160.92 |            $300.00 |           $684.54 |
|    4 |              $684.54 |          $133.75 |            $400.00 |           $418.29 |
|    5 |              $418.29 |           $81.71 |            $500.00 |             $0.00 |

Small differences from other tables may occur because of rounding.

---

## Why Year 5 Ends at Zero

The final year is particularly important.

The beginning investment is approximately:

$$
$418.29
$$

It earns approximately:

$$
418.29(0.1954)
\approx
$81.71
$$

The total value immediately before the final distribution is therefore:

$$
418.29 + 81.71
==============

$500
$$

The final cash flow is:

$$
$500
$$

Therefore:

$$
500 - 500
=========

\boxed{$0}
$$

The investment has been completely recovered after accounting for the return earned on the outstanding investment balance.

This is not a coincidence. It is a consequence of using the **IRR** as the compound rate of return.

---

## Connection to Loan Amortization

The investment table is mathematically similar to a loan amortization schedule.

For a loan:

$$
\text{Ending Loan Balance}
==========================

\text{Beginning Loan Balance}
+
\text{Interest}
---------------

\text{Payment}
$$

For the investment:

$$
\text{Ending Investment Balance}
================================

\text{Beginning Investment Balance}
+
\text{Investment Return}
------------------------

\text{Cash Flow Received}
$$

The mathematics are essentially the same.

The difference is perspective.

With a loan, the lender provides the initial capital and receives payments.

With an investment, the investor provides the initial capital and receives investment cash flows.

---

## Connecting the Investment Table to NPV

IRR is normally defined as the discount rate that causes NPV to equal zero:

$$
NPV(IRR)=0
$$

or:

$$
0
=

\sum_{t=0}^{n}
\frac{CF_t}{(1+IRR)^t}
$$

The investment table provides another way of understanding the same mathematical relationship.

Starting with the initial investment:

$$
$800
$$

the remaining investment earns exactly the IRR each period.

Cash distributions are then removed from the investment balance.

When the correct IRR is used:

$$
\boxed{
\text{Final Investment Balance}=0
}
$$

after the final cash flow.

Therefore, the two statements:

$$
NPV(IRR)=0
$$

and:

$$
\text{Final Investment Balance at IRR}=0
$$

are two ways of expressing the same underlying financial relationship.

---

## Mental Model

A useful way to think about the process is:

```text
Initial Investment
       │
       ▼
Earn return at the IRR
       │
       ▼
Receive cash distribution
       │
       ▼
Subtract distribution from remaining investment
       │
       ▼
Carry remaining balance into next period
       │
       ▼
Repeat
       │
       ▼
Final cash distribution
       │
       ▼
Remaining Investment = $0
```

The key takeaway is:

> **The IRR is the compound rate of return that can be applied to the outstanding investment balance such that, after accounting for all cash distributions, the remaining investment balance reaches zero after the final cash flow.**

The cash flows are subtracted because they represent money that has been **returned to the investor and is therefore no longer part of the investment balance**.
