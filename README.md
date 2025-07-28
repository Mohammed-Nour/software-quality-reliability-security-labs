# Software Quality, Reliability & Security Labs

This repository contains solutions for 8 comprehensive laboratory assignments covering various aspects of software quality assurance, reliability testing, and security analysis. The labs progress from basic concepts to advanced testing methodologies and security practices.

## 📚 Course Overview

These labs are designed to provide hands-on experience with:

- **Software Quality Metrics**: Static analysis, code complexity, and style checking
- **Testing Methodologies**: Unit testing, integration testing, and end-to-end testing
- **Test Coverage Analysis**: Line coverage, branch coverage, and basis path testing
- **Input Domain Testing**: Boundary value analysis and equivalence partitioning
- **Random Testing**: Property-based testing and mutation testing
- **Performance Testing**: Load testing and performance analysis
- **Security Testing**: Vulnerability assessment and security scanning

## 🗂️ Repository Structure

```log
software-quality-reliability-security-labs/
├── s25-sqr-lab0-poetry-ci-Mohammed-Nour/          # Lab 0: Poetry & CI/CD Setup
├── s25-sqr-lab-1-metrics-Mohammed-Nour/           # Lab 1: Static Analysis & Metrics
├── s25-sqr-lab2-testing-Mohammed-Nour/            # Lab 2: Unit & E2E Testing
├── s25-sqr-lab3-coverage-Mohammed-Nour/           # Lab 3: Test Coverage Analysis
├── s25-sqr-lab4-input-Mohammed-Nour/              # Lab 4: Input Domain Testing
├── s25-sqr-lab5-random-testing-Mohammed-Nour/     # Lab 5: Random & Mutation Testing
├── s25-sqr-lab6-performance-Mohammed-Nour/        # Lab 6: Performance Testing
└── s25-sqr-lab7-security-Mohammed-Nour/           # Lab 7: Security Testing
```

## 🧪 Lab Descriptions

### Lab 0: Poetry & CI/CD Setup

**Technologies**: Poetry, GitHub Actions, pytest

- Set up Python project dependency management with Poetry
- Implement continuous integration pipeline with GitHub Actions
- Create basic test automation workflow
- **Project**: Hangman Game setup with CI/CD

### Lab 1: Static Analysis & Metrics

**Technologies**: flake8, complexity analysis tools

- Perform static code analysis and style checking
- Calculate cyclomatic complexity metrics
- Implement code quality gates in CI pipeline
- **Project**: Hangman Game quality analysis

### Lab 2: Unit & E2E Testing

**Technologies**: pytest, unittest.mock, pytest-mock

- Develop comprehensive unit tests with proper mocking
- Create end-to-end tests for complete system workflows
- Implement separate CI workflows for different test types
- **Project**: Bank Management System

### Lab 3: Test Coverage Analysis

**Technologies**: pytest-cov, coverage analysis

- Calculate line and branch coverage metrics
- Perform basis path testing analysis
- Achieve minimum 85% combined coverage threshold
- **Project**: Hangman Game coverage optimization

### Lab 4: Input Domain Testing

**Technologies**: API testing, boundary value analysis

- Apply input domain testing methodologies
- Identify and categorize domain vs computational errors
- Test API endpoints with various input combinations
- **Project**: InnoDrive car-sharing service testing

### Lab 5: Random & Mutation Testing

**Technologies**: mutmut, Hypothesis, property-based testing

- Implement mutation testing to improve test quality
- Apply random testing with property-based approaches
- Analyze mutation survival rates and test effectiveness
- **Projects**: Task Manager (mutation) + InnoDrive (random testing)

### Lab 6: Performance Testing

**Technologies**: Locust, load testing

- Create performance testing suites with Locust
- Analyze synchronous, asynchronous, and cached endpoints
- Measure failure rates and performance characteristics
- **Project**: WikiFet service performance analysis

### Lab 7: Security Testing

**Technologies**: Bandit, security vulnerability scanning

- Identify and fix security vulnerabilities
- Implement security scanning in CI pipeline
- Apply secure coding practices
- **Project**: Electronics shop website security assessment

## 🛠️ Technologies Used

- **Language**: Python 3.8+
- **Dependency Management**: Poetry
- **Testing Frameworks**: pytest, unittest
- **Mocking**: unittest.mock, pytest-mock
- **Coverage**: pytest-cov
- **Static Analysis**: flake8
- **Mutation Testing**: mutmut
- **Property Testing**: Hypothesis
- **Performance Testing**: Locust
- **Security Scanning**: Bandit
- **CI/CD**: GitHub Actions

## 📊 Key Learning Outcomes

- **Quality Metrics**: Understanding and applying software quality metrics
- **Testing Strategies**: Comprehensive testing approach from unit to system level
- **Automation**: CI/CD pipeline implementation for quality assurance
- **Performance Analysis**: Load testing and performance optimization techniques
- **Security Practices**: Vulnerability assessment and secure coding
- **Industry Tools**: Hands-on experience with professional QA tools

## 📝 Assessment Criteria

Each lab is evaluated based on:

- **Correctness**: Proper implementation of testing strategies
- **Coverage**: Meeting minimum coverage thresholds
- **Quality**: Code quality and adherence to best practices
- **Automation**: Successful CI/CD pipeline implementation
- **Documentation**: Clear and comprehensive documentation

## 🔗 External Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [pytest Documentation](https://docs.pytest.org/)
- [Locust Documentation](https://docs.locust.io/)
- [Bandit Security Linter](https://bandit.readthedocs.io/)
- [Testing Python Applications](https://testdriven.io/blog/testing-python/)

---

**Course**: Software Quality, Reliability & Security  
**Institution**: Innopolis University  
**Student**: Mohammed Nour  
**Academic Year**: 2024-2025
