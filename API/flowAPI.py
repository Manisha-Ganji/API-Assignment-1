# URL - https://app.prefect.cloud/account/1d41fc5f-7f44-4380-ac43-4ea4ccce4bf0/workspace/f47716bb-0023-4eed-b03b-6131b4675dce/dashboard

# URL - https://app.prefect.cloud/api/docs

import requests
import json

# Replace these variables with your actual Prefect Cloud credentials
PREFECT_API_KEY = "pnu_WSRFOtLax8Ach0w8pjyGjL6vozB82g0xSCv8"  # Your Prefect Cloud API key
ACCOUNT_ID = "1d41fc5f-7f44-4380-ac43-4ea4ccce4bf0"  # Your Prefect Cloud Account ID
WORKSPACE_ID = "f47716bb-0023-4eed-b03b-6131b4675dce"  # Your Prefect Cloud Workspace ID
FLOW_ID = "a8a07622-f4d1-4e01-9b1c-31e614f58eec"  # Your Flow ID

# Correct API URL to get flow details
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/flows/{FLOW_ID}"
print(PREFECT_API_URL)

# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request using GET
response = requests.get(PREFECT_API_URL, headers=headers)

# Check the response status
if response.status_code == 200:
    flow_info = response.json()
    print("\n\n")
    print(flow_info)
    print(f"\n\nFlow id : {flow_info['id']}")
    print(f"\n\nFlow name : {flow_info['name']}")
    print(f"\n\nFlow is created on : {flow_info['created']}")
    print(f"\n\nFlow is updated on : {flow_info['updated']}")
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")