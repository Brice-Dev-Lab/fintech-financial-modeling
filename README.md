# Financial Modeling with Python

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/badge/package%20manager-uv-blueviolet.svg)](https://docs.astral.sh/uv/)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-Ruff-D7FF64.svg)](https://docs.astral.sh/ruff/)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy-lang.org/)
[![Tests: pytest](https://img.shields.io/badge/tests-pytest-yellow.svg)](https://pytest.org/)
[![Status](https://img.shields.io/badge/status-learning%20project-orange.svg)](#)

A Python-based learning project following **_Financial Modeling_ by Simon Benninga and Tal Mofkadi**.

The purpose of this repository is to work through the financial modeling concepts presented in the book while implementing models, calculations, and analytical workflows in **Python instead of Excel where appropriate**.

This project is part of `dev_lab` and is intended primarily for learning, experimentation, and developing a deeper understanding of financial modeling through software.

---

## Objectives

The primary objectives of this project are to:

- Develop a practical understanding of financial modeling concepts.
- Translate spreadsheet-based financial models into Python where Python provides an appropriate alternative.
- Strengthen the connection between financial theory, mathematical formulation, and implementation.
- Practice using Python for financial analysis and quantitative modeling.
- Explore numerical methods, simulation, optimization, and data analysis techniques used in finance.
- Develop reusable knowledge that may later inform production-oriented financial applications.

The goal is **not to mechanically reproduce Excel worksheets in Python**.

Instead, each implementation should consider how the underlying financial model can be expressed naturally and clearly using Python.

---

## Approach

Exercises generally follow the progression:

```text
Financial concept
      ↓
Understand the mathematical model
      ↓
Review the book's Excel implementation
      ↓
Determine whether Python is appropriate
      ↓
Implement the model
      ↓
Validate the results
      ↓
Interpret the financial meaning
```

Excel may still be used when it provides value for understanding the original example or validating results.

Python implementations should emphasize:

- clarity
- correctness
- reproducibility
- numerical validation
- financial interpretation

---

## Technology

Primary tools may include:

- Python
- NumPy
- pandas
- SciPy
- Matplotlib
- Jupyter
- pytest

Additional libraries may be introduced as the material progresses.

---

## Project Structure

The repository is organized around book exercises, supporting datasets, Python implementations, notebooks, tests, and project documentation.

The canonical project structure and directory responsibilities are documented in:

`docs/01_architecture/00_structure.md`

That document should be treated as the source of truth for repository organization rather than duplicating the complete directory structure here.

---

## Learning Philosophy

The objective is not simply to obtain the same numerical answer as the spreadsheet.

For each model, the implementation should answer four questions:

1. **What financial problem is being modeled?**
2. **What mathematical relationships define the model?**
3. **How should those relationships be implemented computationally?**
4. **What do the results mean financially?**

A successful exercise therefore includes both a correct implementation and an understanding of the model's assumptions, limitations, and interpretation.

---

## From Learning to Application

This repository is a **development laboratory**, not a production financial application.

Concepts developed here may eventually lead to reusable components or ideas for projects maintained elsewhere under `financial_projects`.

When that happens, the production implementation should be developed independently with appropriate:

- architecture
- testing
- validation
- documentation
- error handling
- interfaces
- software engineering standards

The original exercise should remain here as part of the learning record.

---

## Reference

**Benninga, Simon, and Tal Mofkadi. _Financial Modeling_.**

Exercises and implementations in this repository are independent Python implementations created for educational purposes while studying the book.
