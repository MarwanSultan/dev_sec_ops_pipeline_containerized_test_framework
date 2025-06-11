# DevSecOps Pipeline Containerized Test Framework

This repository demonstrates a simple and effective DevSecOps pipeline that integrates security into every stage of the CI/CD process.

## Overview

This project showcases how to:

- Build a CI/CD pipeline using GitHub Actions
- Integrate security testing tools (e.g., SAST, dependency scanning)
- Use Docker to create consistent test environments
- Apply security best practices throughout development and deployment

## Project Structure


## Tools Used

- **GitHub Actions** — CI/CD automation
- **Docker** — containerized testing environment
- **Bandit** (Python SAST) / **Trivy** (container scanning)

## How to Run

To build and test locally using Docker:

```bash
docker build -t devsecops-app .
docker run --rm devsecops-app
