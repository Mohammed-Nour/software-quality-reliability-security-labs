[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/N8-5qFeR)
# Lab Performance

The goal of this lab is to use **Locust** to create a simple testing suite for the WikitFet service.

## WikiFet Service Overview

WikiFet is a unique service designed to extract specific sections from a large text corpus. Each section consists of approximately 200 words. By specifying a section number (ranging from 1 to 530), the service returns the corresponding section from its database.

## Service Capabilities

WikiFet offers four primary routes for accessing its data, each with distinct operational characteristics:

### Route Descriptions

1. **Synchronous, Asynchronous, and Cached Routes**: The first three routes (numbered 1 through 3) differ in their processing mode. One operates synchronously, another asynchronously, and the third one incorporates caching. <u>The task is to evaluate the performance of each route using Locust to determine which route corresponds to each operational mode.</u>

2. **Route with Known Failure Rate**: The fourth route is distinct because it has a known failure rate. <u>The task involves using Locust to assess this route's failure rate</u>, which must be documented as a percentage (e.g., 65 for a 65% failure rate). A tolerance margin of ±3% is allowed for the reported failure rate.

>Note: The Failure Rate is defined as percentatage of failed requests or Nb failures per Nb of requests (f/rqs). You may need to calculate that manually after running a simulation for a substantial amount of time.

## How to Use the Service

### Setting Up WikiFet

To get started with WikiFet, follow these steps to set up the service using Docker:

1. Download the WikiFet Docker image:

    ```bash
    docker pull sh1co/wikifet
    ```

2. Run the WikiFet container, ensuring the appropriate port binding:

    ```bash
    docker run -p 5000:5000 sh1co/wikifet:latest
    ```

**🔴Warning🔴 Due to some limitations, there is a rate limit of 10 requests per second (Set number of users in Locust to <= 10), if the rate limit is exceeded the server will start giving failures which will ruin your results.**

### API Usage

- **Routes 1 to 3**: Use the route pattern `/{email}/fetch/{route_id}/{number}` where `email` is your Innopolis email, `route_id` is the route number (1-3), and `number` is the section number (1-530).

- **Route 4 (Failure Rate Testing)**: Use the route `/{email}/failure/fetch/{number}` with your Innopolis email and the section number (1-530).

### Submitting Your Work

- **Task 1**: Document your findings in `results.csv`, mapping each route (sync, async, cache) to its corresponding route_id. **(6pts)**

- **Task 2**: Record the failure rate of the fourth route in `results.csv` under `failure_rate` without including the percentage symbol. **(3pts)**

- Provide a `locustfile.py` in your repository root containing the tasks for both Task 1 and Task 2 testing. **(3pts)**

Example `results.csv` format:

```
sync,async,cache,failure_rate
1,2,3,65
```

## Resrouces

- [Locust Docs](https://docs.locust.io/en/stable/)
- [Locust Docs/ Creating the first test](https://docs.locust.io/en/stable/quickstart.html)
