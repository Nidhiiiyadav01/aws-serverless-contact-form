# AWS Serverless Contact Form

## 📌 Overview

A fully functional serverless contact form hosted on AWS. The frontend is deployed using Amazon S3, and the backend is powered by AWS API Gateway and AWS Lambda.

## 🌐 Live Demo

http://my-cloud-form-website.s3-website.eu-north-1.amazonaws.com/

## 🚀 Tech Stack

* HTML, CSS, JavaScript
* AWS S3 (Static Website Hosting)
* AWS API Gateway
* AWS Lambda

## ⚙️ How it Works

1. User fills out the contact form on the website
2. Form data is sent using JavaScript (fetch API)
3. API Gateway receives the HTTP POST request
4. API Gateway triggers the AWS Lambda function
5. Lambda processes the request and returns a response
6. UI displays success or error message dynamically

## 🔥 Features

* Fully serverless architecture (no backend server required)
* Real-time API integration using fetch API
* Clean glassmorphism UI with animated background
* Error handling and user feedback system
* Scalable and cost-efficient cloud deployment

## 📸 Demo

![Project Screenshot](screenshot.png)

## 🏗️ Architecture

Frontend (Hosted on AWS S3)
↓
API Gateway (Handles HTTP Requests)
↓
AWS Lambda (Processes Form Data)

## 🔗 API Endpoint

POST https://a9vnj067g3.execute-api.eu-north-1.amazonaws.com/prod/submit_form_handler

## 📁 Project Structure

│── index.html
│── lambda_function.py
│── screenshot.png
│── README.md

## 🧠 Learning Outcomes

* Built and deployed a serverless web application on AWS
* Integrated frontend with cloud backend using API Gateway
* Worked with AWS Lambda functions for backend processing
* Implemented asynchronous form submission using JavaScript
* Gained hands-on experience with real-world cloud architecture

## ⭐ Key Highlights

* Deployed real-world serverless application on AWS
* Integrated frontend with cloud backend using API Gateway
* Implemented asynchronous communication using fetch API

## 📌 Future Improvements

* Store form submissions in AWS DynamoDB
* Add email notifications using AWS SES
* Improve validation and security (rate limiting, input sanitization)
* Add authentication for secure access
