from locust import HttpUser, task, between
import random


class WikiFetUser(HttpUser):
    wait_time = between(1, 2)

    email = "mo.shahin@innopolis.university"

    @task(1)
    def test_sync_route(self):
        section = random.randint(1, 530)
        self.client.get(f"/{self.email}/fetch/1/{section}")

    @task(1)
    def test_async_route(self):
        section = random.randint(1, 530)
        self.client.get(f"/{self.email}/fetch/2/{section}")

    @task(1)
    def test_cache_route(self):
        section = random.randint(1, 530)
        self.client.get(f"/{self.email}/fetch/3/{section}")

    @task(2)
    def test_failure_route(self):
        section = random.randint(1, 530)
        self.client.get(f"/{self.email}/failure/fetch/{section}")
