\# EC2 Cost Automation



\## Project Overview



This project uses Python and Boto3 to automate the process of finding running EC2 instances in the development environment and generating an estimated monthly cost summary.



\## Features



\- Lists running EC2 instances

\- Filters instances using the `Environment=dev` tag

\- Displays instance ID, name, type, and region

\- Calculates estimated hourly and monthly EC2 costs

\- Displays the total estimated monthly cost



\## Technologies Used



\- Python 3

\- Boto3

\- AWS EC2

\- AWS CLI

\- Git



\## Project Structure



```text

ec2-cost-automation/

├── ec2\_cost\_report.py

├── requirements.txt

└── README.md

