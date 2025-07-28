[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MlEdFbWx)
# Mutation Testing - Practical Assignment 1 (2pts)

## Task Manager Project

In this assignment, you are given a simple **Task Manager** project that supports basic CRUD (Create, Read, Update, Delete) operations on tasks. Your task is to write unit tests for this project and apply **mutation testing** to improve the quality of your tests.

> **Note:** We use **Poetry** for dependency management, **pytest** for running tests, and **mutmut** for mutation testing.

---

### 1. Setup

Ensure you have the required tools installed:

```bash
poetry add pytest
poetry add mutmut
```

---

### 2. Implementation

Write unit tests for the two modules in the project: **Task** and **TaskManager**. Save your tests in the file `./tests/test_taskManager.py`.

> **Note:** Follow the example provided in `./tests/test_taskManager.py` strictly.

---

### 3. Execution

Run your tests using the following command:

```bash
poetry run pytest ./tests/test_taskManager.py
```

---

### 4. Mutation Testing

Run **mutmut** to perform mutation testing:

```bash
poetry run mutmut run --paths-to-mutate ./taskManager/ --runner="pytest tests/test_taskManager.py"
```

---

### 5. Check Results

Use the following commands to view the mutation testing results:

```bash
poetry run mutmut show
poetry run mutmut results
```

---

### 6. Analyze Survived Mutations and Improve Tests

To analyze specific mutations that survived, use:

```bash
poetry run mutmut show <id>
```

> **Note:** Replace `<id>` with the ID of the mutation you want to inspect.

---

### Requirements to Pass

- **Minimum number of mutations to cover with tests:** 20
- Many mutations may not be meaningful. Use `# pragma: no mutate` to exclude them.
- Focus on meaningful mutations and ensure your tests kill them.

---

# Random Testing - Practical Assignment 2 (1pt)

## InnoDrive Problem

InnoDrive is a hypothetical autonomous car-sharing service operating in the Kazan region. It offers two types of cars: **budget** and **luxury**, and two tariff plans:

1. **Minute Plan**: Charges based on the time (per minute) the car is used.
2. **Fixed Price Plan**: Charges a fixed price at the time of reservation. If the driver deviates from the planned route by more than 10% (in distance or duration), the plan switches to the **Minute Plan**.

The **Fixed Price Plan** is only available for **budget cars**. Innopolis residents receive a 10% discount on their rides.

You are part of the QA team at InnoDrive. Your task is to apply **random testing** to the billing application using the `Hypothesis` library to identify anomalies in the **Minute Plan** for both car types.

---

## InnoDrive Service

The InnoDrive app provides two services accessible via the following URL:  
[https://rangeprice.devops-playground.innopolis.university/](https://rangeprice.devops-playground.innopolis.university/)

### Services

1. **`/spec`**: Provides the specification for your individual problem.
   - Replace `you_email` with your Innopolis University email address in lowercase (e.g., `i.ivanov@innopolis.university`).

2. **`/rangeprice`**: Calculates the price for a given ride. The input parameters are:
   - `type={budget|luxury}`: Type of car.
   - `plan={fixed_price|minute}`: Tariff plan.
   - `distance=110`: Actual distance traveled (in km).
   - `planned_distance=100`: Planned distance (in km).
   - `time=110`: Actual time taken (in minutes).
   - `planned_time=100`: Planned time (in minutes).
   - `inno_discount={yes|no}`: Whether the Innopolis discount applies.

   **Output**: The calculated price based on the specification.

   **Errors**:
   - If there is an error in the value (e.g., invalid input), the API returns `406 Not Acceptable` with the error code: `Price == -1`.
   - If there is an error in the type (e.g., invalid data type), the API returns `422 Unprocessable Entity`.

> **Note:** You can test the API and explore its functionality at:  
> [https://rangeprice.devops-playground.innopolis.university/docs](https://rangeprice.devops-playground.innopolis.university/docs)

---

## Tasks

Customers have reported anomalies in the **Minute Plan** for both car types. The input space is vast, and exhaustive testing is impractical. Using the `Hypothesis` library, identify at least one failing test case for the **time** parameter in the range of **1-1000 minutes**. Prevent exhaustive search and minimize executions.

> **Note:** Save your tests in `./tests/test_innodrive.py` and strictly follow the provided example.

**Email:** <mo.shahin@innopolis.university>

> **Note:** Replace the email with your Innopolis email.

---

### Error in the Time Range

Replace each `___` with the **time** parameter value (in minutes) for which a failure occurred. Example: `(100)`.

- **Budget Plan Failure on Time =** (790)
- **Luxury Plan Failure on Time =** (124)

---

# Useful Resources

- [Testing Python Applications](http://testdriven.io/blog/testing-python/)
- [mutmut Documentation](https://mutmut.readthedocs.io/en/latest/)
- [Hypothesis Documentation](https://hypothesis.readthedocs.io/en/latest/)
- [Testing with Hypothesis](https://www.inspiredpython.com/course/testing-with-hypothesis/testing-your-python-code-with-hypothesis)


