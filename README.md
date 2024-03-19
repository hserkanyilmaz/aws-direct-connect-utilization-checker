# AWS Direct Connect Utilization Checker

This script helps identify potentially unused AWS Direct Connect connections by analyzing their CloudWatch metrics over the past 30 days.

### Prerequisites

Before running this script, ensure you have the following:

* AWS CLI installed and configured with the necessary access rights to list Direct Connect connections and retrieve CloudWatch metrics. AWS CLI Installation Guide
* Python 3.x installed on your system.
* Boto3 library installed. You can install it using pip:

```bash
pip install boto3
```

### Setting Up

Configure AWS CLI:

If not already configured, set up your AWS CLI by running:

```bash
aws configure
```

Enter your AWS Access Key ID, Secret Access Key, region, and output format as prompted.

### Usage

To use the AWS Direct Connect Utilization Checker script, follow these steps:

* Open a terminal or command prompt and change to the directory where the script is located.

Run the script:

Execute the script with Python:

```bash
export AWS_DEFAULT_REGION=us-east-1

python aws_dx_utilization_checker.py
```

Review the output:

* The script outputs the average DataInRate and DataOutRate for each Direct Connect connection over the specified period.
* Connections with no data points for the metrics might not be in use and can be candidates for further investigation or decommissioning.

### Notes

* **Monitoring Period:** The script is set to analyze the last 7 days. Modify the start_time and end_time variables in the script to adjust this period according to your needs.
* **AWS Permissions:** Ensure your AWS IAM user or role has sufficient permissions to access Direct Connect and CloudWatch metrics.
* **Feedback:** For any issues, suggestions, or improvements, please share your feedback with the team or contribute to the script directly.

### Contributing

Your contributions are welcome! Please follow the standard GitHub pull request process to submit your enhancements or fixes.
