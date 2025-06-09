# Database Automation and CI/CD Pipeline

This repository contains scripts and workflows for automating database schema changes and implementing CI/CD for database deployment.

## Project Structure

- `create_projects_table.sql`: SQL script for creating and modifying the projects table
- `add_departments.sql`: SQL script for creating the departments table
- `execute_sql.py`: Python script to execute SQL commands
- `.github/workflows/ci_cd_pipeline.yml`: GitHub Actions workflow for database deployment
- `requirements.txt`: Python dependencies

## Setup Instructions

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure database connection:
   - Update the database connection parameters in `execute_sql.py`
   - Set up GitHub repository secrets for CI/CD:
     - DB_HOST
     - DB_USER
     - DB_PASSWORD
     - DB_NAME

## Azure MySQL Setup

1. Create an Azure MySQL Database:
   - Log in to Azure Portal
   - Create a new MySQL server
   - Create a new database named 'companydb'
   - Configure firewall rules
   - Note down the connection details

2. Configure GitHub Secrets:
   - Go to your GitHub repository
   - Navigate to Settings > Secrets
   - Add the following secrets:
     - DB_HOST: Your Azure MySQL server hostname
     - DB_USER: Database username
     - DB_PASSWORD: Database password
     - DB_NAME: companydb

## Testing the Workflow

1. Push changes to the main branch
2. Monitor the GitHub Actions workflow
3. Verify the database changes in Azure MySQL

## Documentation

For detailed documentation including screenshots and step-by-step instructions, please refer to the `documentation.pdf` file in the repository. 