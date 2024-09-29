# URL - https://app.prefect.cloud/account/1d41fc5f-7f44-4380-ac43-4ea4ccce4bf0/workspace/f47716bb-0023-4eed-b03b-6131b4675dce/dashboard

# Ref - https://app.prefect.cloud/api/docs

import requests

# Replace these variables with your actual Prefect Cloud credentials
PREFECT_API_KEY = "pnu_YtZWDV5docvM1I1XpQysa3EH1EKkqM4CtdAW"  # Your Prefect Cloud API key
ACCOUNT_ID = "1d41fc5f-7f44-4380-ac43-4ea4ccce4bf0"  # Your Prefect Cloud Account ID
WORKSPACE_ID = "f47716bb-0023-4eed-b03b-6131b4675dce"  # Your Prefect Cloud Workspace ID

# Correct API URL to list flow runs
PREFECT_API_URL = f"https://api.prefect.cloud/api/accounts/{ACCOUNT_ID}/workspaces/{WORKSPACE_ID}/artifacts/filter"

# Data to filter artifacts
data = {
    "sort": "CREATED_DESC",
    "limit": 5,
    "artifacts": {
        "key": {
            "exists_": True
        }
    }
}

# Set up headers with Authorization
headers = {"Authorization": f"Bearer {PREFECT_API_KEY}"}

# Make the request
response = requests.post(PREFECT_API_URL, headers=headers, json=data)
print(response)

# Check the response status
if response.status_code != 200:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
else:
    artifacts = response.json()
    print(artifacts)
    for artifact in artifacts:
        print(artifact)
