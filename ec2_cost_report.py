import boto3

REGION = "ap-south-1"

# Estimated hourly prices
INSTANCE_PRICES = {
    "t3.micro": 0.0112,
    "t3.small": 0.0208,
    "t3.medium": 0.0416
}

ec2 = boto3.client("ec2", region_name=REGION)

response = ec2.describe_instances(
    Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"]
        }
    ]
)

print("EC2 COST ESTIMATE")
print("=================")
print("Environment: dev")
print()

total_monthly_cost = 0
instance_count = 0

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:

        environment = ""
        name = "No Name"

        for tag in instance.get("Tags", []):
            if tag["Key"] == "Environment":
                environment = tag["Value"].strip().lower()
            elif tag["Key"] == "Name":
                name = tag["Value"]

        if environment == "dev":

            instance_count += 1

            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]

            hourly_cost = INSTANCE_PRICES.get(instance_type, 0)
            monthly_cost = hourly_cost * 24 * 30

            total_monthly_cost += monthly_cost

            print(f"Instance ID : {instance_id}")
            print(f"Name        : {name}")
            print(f"Type        : {instance_type}")
            print(f"Hourly Cost : ${hourly_cost:.4f}")
            print(f"Monthly Cost: ${monthly_cost:.2f}")
            print("-------------------------")

print()
print(f"Total Running Dev Instances: {instance_count}")
print(f"Estimated Monthly Cost     : ${total_monthly_cost:.2f}")