# This is the template for the InnoDrive e2e and domain and computation test cases.

import pytest
from httpx import Client

EMAIL = "mo.shahin@innopolis.university"

spec = {
  "budget_minute_price": 19,
  "luxury_minute_price": 57,
  "budget_km_price": 17,
  "deviation": 0.07,
  "inno_discount": 0.2
}


@pytest.fixture(scope="module")
def test_app():
    client = Client(base_url="https://innodrive.devops-playground.innopolis.university", verify=False)
    yield client  # testing happens here


@pytest.mark.parametrize("email", [EMAIL])
def test_spec(test_app, email):
    response = test_app.get("/spec/"+email)

    assert response.status_code == 200
    assert response.json() == spec


# Domain Tests
not_acceptable_params = [
    {
        "type": "",
        "plan": "minute",
        "distance": 110,
        "planned_distance": 100,
        "time": 110,
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "",
        "distance": 110,
        "planned_distance": 100,
        "time": 110,
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": -1,
        "planned_distance": 110,
        "time": 110,
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": 110,
        "planned_distance": -1,
        "time": 110,
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": 110,
        "planned_distance": 100,
        "time": -1,
        "planned_time": 110,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": 110,
        "planned_distance": 110,
        "time": 110,
        "planned_time": -1,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": 10001,
        "planned_distance": 100,
        "time": 110,
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": 110,
        "planned_distance": 10001,
        "time": 110,
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": 110,
        "planned_distance": 100,
        "time": 10001,
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": 110,
        "planned_distance": 100,
        "time": 110,
        "planned_time": 10001,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": 110,
        "planned_distance": 100,
        "time": 110,
        "planned_time": 100,
        "inno_discount": "",
    },
    {
        "type": "luxury",
        "plan": "fixed_price",
        "distance": 110,
        "planned_distance": 100,
        "time": 110,
        "planned_time": 100,
        "inno_discount": "no",
    },
]


not_processable_params = [
    {
        "type": 0,
        "plan": "minute",
        "distance": 110,
        "planned_distance": 100,
        "time": 110,
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": 0,
        "distance": 110,
        "planned_distance": 100,
        "time": 110,
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "fixed_price",
        "distance": "",
        "planned_distance": 100,
        "time": 110,
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "fixed_price",
        "distance": 110,
        "planned_distance": "",
        "time": 110,
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": 110,
        "planned_distance": 100,
        "time": "",
        "planned_time": 100,
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": 110,
        "planned_distance": 100,
        "time": 110,
        "planned_time": "",
        "inno_discount": "no",
    },
    {
        "type": "budget",
        "plan": "minute",
        "distance": 110,
        "planned_distance": 100,
        "time": 110,
        "planned_time": 100,
        "inno_discount": 0,
    },
]

@pytest.mark.parametrize("email", [EMAIL])
@pytest.mark.parametrize("request_body", not_acceptable_params)
def test_not_acceptable_params_requests(test_app, email, request_body):
    response = test_app.post(f"/price/{email}", json=request_body)
    assert response.status_code == 406


@pytest.mark.parametrize("email", [EMAIL])
@pytest.mark.parametrize("request_body", not_processable_params)
def test_not_proccable_params_requests(test_app, email, request_body):
    response = test_app.post(f"/price/{email}", json=request_body)
    assert response.status_code == 422

# Computation Tests


computational_params = [
    # 1. luxury, minute plan, no discount
    {
        "input": {
            "type": "luxury",
            "plan": "minute",
            "distance": 110,
            "planned_distance": 100,
            "time": 10,
            "planned_time": 110,
            "inno_discount": "no",
        },
        "expected_price": 10 * spec["luxury_minute_price"]
    },
    {
        "input": {
            "type": "luxury",
            "plan": "minute",
            "distance": 110,
            "planned_distance": 100,
            "time": 1,
            "planned_time": 100,
            "inno_discount": "no",
        },
        "expected_price": 1 * spec["luxury_minute_price"]
    },
    {
        "input": {
            "type": "luxury",
            "plan": "minute",
            "distance": 110,
            "planned_distance": 100,
            "time": 2000,
            "planned_time": 1000,
            "inno_discount": "no",
        },
        "expected_price": 2000 * spec["luxury_minute_price"]
    },
    {
        "input": {
            "type": "luxury",
            "plan": "minute",
            "distance": 100,
            "planned_distance": 110,
            "time": 10000,
            "planned_time": 100,
            "inno_discount": "no",
        },
        "expected_price": 10000 * spec["luxury_minute_price"]
    },
    {
        "input": {
            "type": "luxury",
            "plan": "minute",
            "distance": 1,
            "planned_distance": 2,
            "time": 10000,
            "planned_time": 1,
            "inno_discount": "no",
        },
        "expected_price": 10000 * spec["luxury_minute_price"]
    },
    # 2. luxury, minute plan, discount
    {
        "input": {
            "type": "luxury",
            "plan": "minute",
            "distance": 110,
            "planned_distance": 100,
            "time": 100,
            "planned_time": 110,
            "inno_discount": "yes",
        },
        "expected_price": 100 * spec["luxury_minute_price"] - ((100 * spec["luxury_minute_price"]) * spec["inno_discount"])
    },
    # 3. budget, minute plan, no discount
    {
        "input": {
            "type": "budget",
            "plan": "minute",
            "distance": 100,
            "planned_distance": 110,
            "time": 100,
            "planned_time": 100,
            "inno_discount": "no",
        },
        "expected_price": 100 * spec["budget_minute_price"]
    },
    # 4. budget, minute plan, discount
    {
        "input": {
            "type": "budget",
            "plan": "minute",
            "distance": 110,
            "planned_distance": 110,
            "time": 120,
            "planned_time": 120,
            "inno_discount": "yes",
        },
        "expected_price": 120 * spec["budget_minute_price"] - ((120 * spec["budget_minute_price"]) * spec["inno_discount"])
    },
    # 5. budget, fixed_price plan, no discount, no deviation
    {
        "input": {
            "type": "budget",
            "plan": "fixed_price",
            "distance": 500,
            "planned_distance": 500,
            "time": 150,
            "planned_time": 150,
            "inno_discount": "no",
        },
        "expected_price": 500 * spec["budget_km_price"]
    },
    # 6. budget, fixed_price plan, no discount, deviation time
    {
        "input": {
            "type": "budget",
            "plan": "fixed_price",
            "distance": 100,
            "planned_distance": 100,
            "time": 120,
            "planned_time": 100,
            "inno_discount": "no",
        },
        "expected_price": 120 * spec["budget_minute_price"]
    },
    # 7. budget, fixed_price plan, no discount, with distance deviation
    {
        "input": {
            "type": "budget",
            "plan": "fixed_price",
            "distance": 1080,
            "planned_distance": 1000,
            "time": 100,
            "planned_time": 100,
            "inno_discount": "no",
        },
        "expected_price": 100 * spec["budget_minute_price"]
    },
    # 8. budget, fixed_price plan, discount, with distance deviation
    {
        "input": {
            "type": "budget",
            "plan": "fixed_price",
            "distance": 1080,
            "planned_distance": 1000,
            "time": 100,
            "planned_time": 100,
            "inno_discount": "yes",
        },
        "expected_price": 100 * spec["budget_minute_price"] - ((100 * spec["budget_minute_price"]) * spec["inno_discount"])
    },
    # 9. budget, fixed_price plan, discount, with deviation time
    {
        "input": {
            "type": "budget",
            "plan": "fixed_price",
            "distance": 1000,
            "planned_distance": 1000,
            "time": 150,
            "planned_time": 100,
            "inno_discount": "yes",
        },
        "expected_price": 150 * spec["budget_minute_price"] - ((150 * spec["budget_minute_price"]) * spec["inno_discount"])
    },
    {
        "input": {
            "type": "budget",
            "plan": "fixed_price",
            "distance": 1000,
            "planned_distance": 1000,
            "time": 1060,
            "planned_time": 1000,
            "inno_discount": "yes",
        },
        "expected_price": 1000 * spec["budget_km_price"] - ((1000 * spec["budget_km_price"]) * spec["inno_discount"])
    },
    {
        "input": {
            "type": "budget",
            "plan": "fixed_price",
            "distance": 1060,
            "planned_distance": 1000,
            "time": 1060,
            "planned_time": 1000,
            "inno_discount": "yes",
        },
        "expected_price": 1000 * spec["budget_km_price"] - ((1000 * spec["budget_km_price"]) * spec["inno_discount"])
    },
    {
        "input": {
            "type": "budget",
            "plan": "fixed_price",
            "distance": 1080,
            "planned_distance": 1000,
            "time": 1060,
            "planned_time": 1000,
            "inno_discount": "yes",
        },
        "expected_price": 1060 * spec["budget_minute_price"] - ((1060 * spec["budget_minute_price"]) * spec["inno_discount"])
    },
    {
        "input": {
            "type": "budget",
            "plan": "fixed_price",
            "distance": 1000,
            "planned_distance": 1000,
            "time": 1080,
            "planned_time": 1000,
            "inno_discount": "yes",
        },
        "expected_price": 1080 * spec["budget_minute_price"] - ((1080 * spec["budget_minute_price"]) * spec["inno_discount"])
    },
]

@pytest.mark.parametrize("email", [EMAIL])
@pytest.mark.parametrize("test_case", computational_params)
def test_computational_correctness(test_app, test_case, email):
    response = test_app.post(f"/price/{email}", json=test_case["input"])
    assert response.status_code == 200

    result = response.json()
    actual = result["price"]
    expected = test_case["expected_price"]

    assert actual == expected, f"Expected: {expected}, Got: {actual}"
