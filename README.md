# Assignment 2: Database Automation and CI/CD Pipeline

## Overview
This project implements database schema automation and CI/CD pipeline for Azure MySQL database deployment.

## Step-by-Step Implementation

### 1. Azure MySQL Setup
1. Create Azure MySQL Server:
   - Server name: companysqll
   - Database name: companydb
   - Username: CompanyServers
   - Password: companyservers@123

2. Configure Firewall:
   - Allow your IP address
   - Enable public access

3. Download SSL Certificate:
   - Save as DigiCertGlobalRootCA.crt.pem

### 2. Project Structure
- .github/workflows/ci_cd_pipeline.yml
- create_projects_table.sql
- add_departments.sql
- execute_sql.py
- requirements.txt
- DigiCertGlobalRootCA.crt.pem


### 3. Database Schema Implementation

#### Projects Table (create_projects_table.sql)
```sql
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);

ALTER TABLE projects
ADD COLUMN budget DECIMAL(10, 2);
```

#### Departments Table (add_departments.sql)
```sql
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL,
    location VARCHAR(255)
);
```

### 4. Python Implementation (execute_sql.py)
- Connects to Azure MySQL using SSL
- Executes SQL scripts
- Handles errors and commits changes

### 5. CI/CD Pipeline Setup

#### GitHub Actions Workflow (.github/workflows/ci_cd_pipeline.yml)
- Triggers on push to main branch
- Sets up Python environment
- Installs dependencies
- Executes SQL scripts

#### GitHub Secrets Configuration
DB_HOST: companysqll.mysql.database.azure.com
DB_USER: CompanyServers
DB_PASSWORD: Test@123
DB_NAME: companydb

### 6. Testing Process

#### Local Testing
1. Install dependencies:
   pip install -r requirements.txt

2. Run the script:
   python execute_sql.py

3. Verify in Azure MySQL:
   - Check projects table
   - Check departments table

#### CI/CD Testing
1. Push changes to main branch
2. Monitor GitHub Actions workflow
3. Verify database changes