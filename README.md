# AWS Serverless Contact Form

## 📌 Overview
A fully functional serverless contact form hosted on AWS. The frontend is deployed using Amazon S3, and the backend is powered by AWS API Gateway and AWS Lambda.

## 🌐 Live Demo
http://my-cloud-form-website.s3-website.eu-north-1.amazonaws.com/

## 🚀 Tech Stack
- HTML, CSS, JavaScript
- AWS S3 (Static Website Hosting)
- AWS API Gateway
- AWS Lambda

## ⚙️ How it Works
1. User submits form on frontend (hosted on S3)
2. JavaScript sends POST request to API Gateway
3. API Gateway triggers AWS Lambda function
4. Lambda processes request and returns response
5. UI displays success/error message dynamically

## 🔥 Features
- Fully serverless architecture
- Real-time API integration
- Animated glassmorphism UI
- Async form handling with fetch API
- Error handling and user feedback

## 📁 Project Structure
│── index.html  
│── README.md  

## 🧠 Learning Outcomes
- Built and deployed serverless architecture on AWS
- Integrated frontend with API Gateway
- Worked with Lambda functions and HTTP APIs
- Learned real-world deployment using S3

## 📌 Future Improvements
- Store submissions in DynamoDB
- Add email notifications using AWS SES
- Improve security (validation, rate limiting)
