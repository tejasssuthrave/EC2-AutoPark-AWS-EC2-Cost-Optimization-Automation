# 🚗 EC2 AutoPark – AWS EC2 Cost Optimization Automation

EC2 AutoPark is an AWS automation project that automatically starts and stops EC2 instances on a defined schedule using Amazon EventBridge, AWS Lambda, and Amazon SNS.  
This project helps reduce unnecessary AWS EC2 costs by ensuring instances run only during required working hours.

---

## 📌 Problem Statement

- EC2 instances are started manually
- Instances are often forgotten and left running
- Instances run overnight and on weekends
- This leads to unnecessary AWS billing

---

## ✅ Solution

This project provides a fully serverless automation that:

- Starts EC2 instances automatically in the morning
- Stops EC2 instances automatically at night
- Runs only on weekdays (Monday–Friday)
- Sends email notifications on instance start and stop
- Uses only AWS-native services

---

## 🏗 Architecture Diagram

```mermaid
flowchart TD
    A[Amazon EventBridge Scheduler] --> B[AWS Lambda]
    B --> C[Amazon EC2 Instances]
    B --> D[Amazon SNS]
    D --> E[Email Notification]
