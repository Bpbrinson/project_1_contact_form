# project_1_contact_form

Description:
Developed a production-ready, cloud-native contact form web application using Flask and AWS services to demonstrate full-stack development and DevOps proficiency. The application captures user input (name, email, message), stores submissions in a secure AWS RDS MySQL database, and sends real-time email alerts using AWS Simple Email Service (SES).

The application is containerized with Docker and deployed using AWS ECS Fargate, ensuring scalable and serverless infrastructure. The entire cloud environment, including VPC, RDS, ECS services, and IAM roles, is provisioned using Terraform as Infrastructure as Code (IaC). Automated deployments are configured through a CI/CD pipeline built with GitHub Actions, enabling seamless updates from code commit to production.

