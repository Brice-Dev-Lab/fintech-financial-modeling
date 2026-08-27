# Internal Rate of Return (IRR)

## Core Concept

The **Internal Rate of Return (IRR)** is the rate of return implied by an investment's own cash flows.

It is the discount rate that causes the investment's **Net Present Value (NPV) to equal zero**:

$$
0
=
\sum_{t=0}^{n}
\frac{CF_t}{(1+IRR)^t}
$$

The most useful way to think about IRR is:

> **IRR tells you what the investment earns. The discount rate tells you what you require it to earn.**

---

## IRR vs. Required Return

Suppose an investment has:

$$
IRR = 17%
$$

Think of this as saying:

> **The investment's cash flows imply a 17% rate of return.**

Now compare that return with the **required rate of return**, or hurdle rate.

|     IRR | Required Return | Result         |
| ------: | --------------: | -------------- |
|     17% |              5% | Accept         |
|     17% |             10% | Accept         |
|     17% |             15% | Accept         |
| **17%** |         **17%** | **Break-even** |
|     17% |             20% | Reject         |
|     17% |             25% | Reject         |

The investment itself has not changed. It still produces a 17% IRR.

What changes is the return that the investor requires.

---

## Why a 10% Required Return Is Good

Suppose:

$$
IRR = 17%
$$

and:

$$
r_{\text{required}} = 10%
$$

Then:

$$
17% > 10%
$$

The investment provides a higher return than required.

Therefore:

$$
NPV > 0
$$

The investment creates value beyond the required return.

---

## Why a 20% Required Return Is Bad

Suppose the same investment has:

$$
IRR = 17%
$$

but now:

$$
r_{\text{required}} = 20%
$$

Then:

$$
17% < 20%
$$

The investment does not generate enough return to satisfy the requirement.

Therefore:

$$
NPV < 0
$$

The project itself did not become worse. The required return simply became greater than what the project's cash flows can support.

---

## What "Break-Even" Means

If:

$$
IRR = 17%
$$

then at a required return of exactly 17%:

$$
NPV = 0
$$

This does **not** mean the investment earns nothing.

It means the investment earns **exactly the required return**.

The present value of the future cash flows exactly equals the initial investment.

Therefore:

$$
PV(\text{future cash flows})
===
\text{initial investment}
$$

There is no additional value above the required return, but there is also no shortfall.

---

## Simple One-Year Example

Suppose an investment costs:

$$
$100
$$

today and returns:

$$
$117
$$

one year from now.

The investment's return is:

$$
\frac{117-100}{100}
===
17%
$$

Therefore:

$$
IRR = 17%
$$

### If the required return is 10%

A $100 investment earning 10% would need to return:

$$
100(1.10)
===
$110
$$

But the investment actually returns:

$$
$117
$$

Therefore, it exceeds the required return and is attractive.

### If the required return is 20%

A $100 investment earning 20% would need to return:

$$
100(1.20)
===
$120
$$

But the investment only returns:

$$
$117
$$

Therefore, it fails to meet the required return.

### If the required return is 17%

The required future value is:

$$
100(1.17)
===
$117
$$

This exactly matches the investment's cash flow.

Therefore:

$$
NPV = 0
$$

This is the break-even discount rate.

---

## Relationship Between IRR and NPV

The relationship can be summarized as:

$$
IRR > r_{\text{required}}
\Rightarrow
NPV > 0
\Rightarrow
\text{Accept}
$$

$$
IRR = r_{\text{required}}
\Rightarrow
NPV = 0
\Rightarrow
\text{Break-even}
$$

$$
IRR < r_{\text{required}}
\Rightarrow
NPV < 0
\Rightarrow
\text{Reject}
$$

---

## Mental Model

Keep the two rates separate:

### IRR

> **What does this investment earn?**

The IRR comes from the investment's cash flows.

### Discount Rate / Required Return

> **What do I require this investment to earn?**

The required return comes from the investor, organization, cost of capital, risk requirements, or other decision criteria.

Then simply compare them:

$$
\boxed{IRR \quad \text{vs.} \quad Required\ Return}
$$

The key takeaway is:

> **IRR tells you what the investment earns. The discount rate tells you what you require it to earn.**
