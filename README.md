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
<img width="1536" height="1024" alt="ChatGPT Image Feb 8, 2026, 05_02_24 PM" src="https://github.com/user-attachments/assets/7470d53c-1af6-45e0-af5d-7492807402c3" />


---

## 🧰 AWS Services Used

- Amazon EC2
- AWS Lambda (Python)
- Amazon EventBridge Scheduler
- Amazon SNS
- AWS IAM
- Amazon CloudWatch

---

## ⏰ Scheduling Details

| Action   | Time (IST) | Days            |
|----------|------------|-----------------|
| Start EC2 | 09:00 AM   | Monday – Friday |
| Stop EC2  | 08:00 PM   | Monday – Friday |

### Cron Expressions

- **Start schedule:**  
  `cron(0 9 ? * MON-FRI *)`

- **Stop schedule:**  
  `cron(0 20 ? * MON-FRI *)`

---

## 🏷 EC2 Instance Selection (Tag Based)

Only EC2 instances with the following tag are managed:

- **Key:** AutoPark  
- **Value:** true  

This ensures only intended EC2 instances are started or stopped.

---

## 📬 Email Notifications (SNS)

An email notification is sent whenever an EC2 instance is:

- Started
- Stopped

The email includes:
- Instance ID
- Instance Name
- Public IP Address
- Action performed (START / STOP)
- Timestamp

---

## 🔐 IAM Permissions

The Lambda execution role includes the following permissions:

- ec2:DescribeInstances
- ec2:StartInstances
- ec2:StopInstances
- sns:Publish
- logs:CreateLogGroup
- logs:CreateLogStream
- logs:PutLogEvents

---

## 💰 Cost Optimization Benefits
- Prevents EC2 instances from running during off-hours
- Ideal for development and testing environments
- Reduces monthly AWS costs
- Fully serverless solution with minimal operational overhead

--- 

## 📈 Future Enhancements
- SMS or WhatsApp notifications
- Slack integration
- Auto Scaling Group support
- Multi-region scheduling
- Infrastructure as Code (Terraform / CloudFormation)

