# 📧 Serverless Email Sender API (Python)

This project sets up a RESTful API using the Serverless Framework and AWS Lambda with Python. It allows users to send emails by providing the recipient's email address, a subject, and body content. It also supports offline development and includes proper error handling with HTTP status codes.

---

## 🔧 Prerequisites

- [Serverless account](https://www.serverless.com/)
- [Node.js & NPM](https://nodejs.org/)
- Python 3.10+
- AWS account and credentials (via `aws configure`)

---

## 🛠 Project Setup

### 1. Install Serverless CLI

```bash
npm install -g serverless

2. Initialize Python Service
```bash
serverless create --template aws-python --path email-api
cd email-api
