# URL - https://app.prefect.cloud/account/1d41fc5f-7f44-4380-ac43-4ea4ccce4bf0/workspace/f47716bb-0023-4eed-b03b-6131b4675dce/dashboard

# URL - https://app.prefect.cloud/api/docs

import requests
import json

# Replace these variables with your actual Prefect Cloud credentials
PREFECT_API_KEY = "pnu_WSRFOtLax8Ach0w8pjyGjL6vozB82g0xSCv8"  # Your Prefect Cloud API key
ACCOUNT_ID = "1d41fc5f-7f44-4380-ac43-4ea4ccce4bf0"  # Your Prefect Cloud Account ID
WORKSPACE_ID = "f47716bb-0023-4eed-b03b-6131b4675dce"  # Your Prefect Cloud Workspace ID
DEPLOYMENT_ID = "37a06923-4096-4fff-b44e-e343fb241c94"  # Your Deployment ID

# Correct API URL to get deployment details
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/deployments/{DEPLOYMENT_ID}"

print(PREFECT_API_URL)
# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request using GET
response = requests.get(PREFECT_API_URL, headers=headers)

# Check the response status
if response.status_code == 200:
    deployment_info = response.json()
    print("\n\n")
    print(deployment_info)
    print(f"\n\nDeployment id : {deployment_info['id']}")
    print(f"\n\nDeployment name : {deployment_info['name']}")
    print(f"\n\nDeployment created on : {deployment_info['created']}")
    print(f"\n\nDeployment is scheduled for : {(deployment_info['schedule'])['interval']} seconds")
    print(f"\n\nDeployment is scheduled as per : {(deployment_info['schedule'])['timezone']} timezone")
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
