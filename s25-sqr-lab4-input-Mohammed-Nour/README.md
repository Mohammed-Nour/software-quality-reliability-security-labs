[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/8Kxkjgpb)
# InnoDrive - Problem

## Introduction

InnoDrive is a hypothetical autonomous car-sharing service operating in the Kazan region. It was developed by SQR graduates from Innopolis University. The service offers two types of cars: **budget** and **luxury**, and provides two tariff plans:

1. **Minute Plan**: The client is charged based on the time (per minute) the car is used.
2. **Fixed Price Plan**: The price is fixed at the time of reservation based on the chosen route. However, if the driver deviates from the planned route by more than 10% (in distance or duration), the plan automatically switches to the **Minute Plan**.

The **Fixed Price Plan** is only available for **budget cars**. Additionally, Innopolis residents receive a 10% discount on their rides.

You are a member of the Quality Assurance (QA) team at InnoDrive. Your task is to apply **input domain testing methods** to the billing application that calculates the price for a ride.

> **Note:** The exact **tariffs**, **deviation percentage**, and **discount percentage** will vary depending on your individual case. Refer to the API specification for your specific values.

---

## InnoDrive Service

The InnoDrive app provides two services accessible via the following URL:  
[https://innodrive.devops-playground.innopolis.university/](https://innodrive.devops-playground.innopolis.university/)

### Services

1. **`spec`**: Provides the specification for your individual problem.
   - Replace `you_email` with your Innopolis University email address in lowercase (e.g., `i.ivanov@innopolis.university`).

2. **`price`**: Calculates the price for a given ride. The input parameters are:
   - `type={budget|luxury}`: Type of car.
   - `plan={fixed_price|minute}`: Tariff plan.
   - `distance=110`: Actual distance traveled (in km) (Max : 10 000).
   - `planned_distance=100`: Planned distance (in km) (Max : 10 000).
   - `time=110`: Actual time taken (in minutes) (Max : 10 000).
   - `planned_time=100`: Planned time (in minutes) (Max : 10 000).
   - `inno_discount={yes|no}`: Whether the Innopolis discount applies.

   **Output**: The calculated price based on the specification.

   **Errors**:
   - If there is an error in the  `value` (e.g., invalid input), the API **must** return `406 Not Acceptable` with the error code: `Price == -1`.
   - If there is an error in the `type` (e.g., invalid data type), the API **must** return `422 Unprocessable Entity`.

> **Note:** You can test the API and explore its functionality at:  
> [https://innodrive.devops-playground.innopolis.university/docs](https://innodrive.devops-playground.innopolis.university/docs)

---

# Practical Assignment

Your task is to develop a comprehensive test suite to evaluate the system's functionality. After identifying errors, categorize them as either **domain errors** or **computational errors**.

## 1. Domain Errors (3 points)

Domain errors occur when the system fails to validate input parameters correctly or does not handle boundaries appropriately. For example, the system accepts invalid inputs instead of rejecting them.

Replace each `-` with `yes` if parameter passes domain tests or `no` if it fails.

- **Ride Type:** yes
- **Ride Plan:** yes  
- **Distance:** no  
- **Inno Discount:** yes
- **Type Plan:** yes  
- **Time:** yes  

> **Note:** "Type Plan" refers to checking the compatibility of the ride type and ride plan (e.g., the Fixed Price Plan is only available for budget cars).

## 2. Computational Errors (3 points)

Computational errors occur when the system accepts valid inputs but produces incorrect results.

Replace each `-` with `yes` if parameter passes computational tests or `no` if it fails.

- **Deviation:** no  
- **Discount Calculation:** yes  
- **Budget Min:** yes  
- **Budget Km:** yes  
- **Luxury Min:** yes  

## 3. Test Coverage (1 points)

Your test suite will be evaluated based on its ability to detect all the errors outlined above.

---

# Additional Information

- **OpenAPI Specification**: You can find the API specification in the provided [`openapi.json`](./openapi.json) file.

---

## Submission Guidelines

1. Save your tests in `./tests/test_innodrive.py`.
2. Ensure your test suite covers all potential errors (domain and computational).
3. Replace the email in the `EMAIL` variable with your Innopolis email.
4. Submit your assignment as per your instructor's instructions.





  



