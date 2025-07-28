# This is the template for the InnoDrive e2e and domain and computation test cases.

import pytest
from hypothesis import given, settings, Phase
import hypothesis.strategies as st

from httpx import Client

email = "mo.shahin@innopolis.university"
@pytest.fixture(scope="module")
def test_app():
    client = Client(base_url="https://rangeprice.devops-playground.innopolis.university/")
    yield client  # testing happens here

@pytest.mark.parametrize("email", [email])
def test_spec(test_app, email):
    response = test_app.get("/spec/"+email)

    assert response.status_code == 200

@settings(max_examples=20, deadline=None)
@given(
    time=st.integers(min)
)
def test_minute_plan_budget_time_range(test_app, time):
    params = {
        "type": "budget",
        "plan": "minute",
        "distance": 100,
        "planned_distance": 100,
        "time": time,
        "planned_time": time,
        "inno_discount": "no"
    }
    response = test_app.post("/rangeprice/"+email, json=params)
    data = response.json()

    assert response.status_code == 200, f"Failed for time={time} with status {response.status_code}"
    assert data["price"] >= 0, f"Invalid price for budget car at time={time}: {data}"
    assert data["price"] == 21 * time, f"Invalid price for budget car at time={time}: {data}"



@settings(max_examples=20, deadline=None)
@given(
    time=st.integers(min_value=1, max_value=20)
)
def test_minute_plan_luxury_time_range(test_app, time):
    params = {
        "type": "luxury",
        "plan": "minute",
        "distance": 100,
        "planned_distance": 100,
        "time": time,
        "planned_time": time,
        "inno_discount": "no"
    }
    response = test_app.post("/rangeprice/"+email, json=params)
    data = response.json()

    assert response.status_code == 200, f"Failed for time={time} with status {response.status_code}"
    assert data["price"] >= 0, f"Invalid price for luxury car at time={time}: {data}"
    assert data["price"] == 50 * time, f"Invalid price for luxury car at time={time}: {data}"
