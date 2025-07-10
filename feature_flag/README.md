# Feature Flags

This is a simple Flask demo that uses [UnleashClient](https://github.com/Unleash/unleash-client-python) to check feature flags via GitLab's Unleash API.

## Quick Start

Copy the commands below to get started!

```sh
# Clone the repository
git clone https://github.com/ishimto/demos.git
cd feature_flag

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python main.py
```

## Endpoints

* ```GET /flag1```
Returns "Flag1 Enabled" if the demo_flag_enable feature flag is enabled, otherwise "Flag1 not enabled".

* ```GET /flag2```
Returns "Flag2 Enabled" if the demo_flag_disable feature flag is enabled, otherwise "Flag2 not enabled".

## Configuration
The Unleash client is configured in main.py with a hardcoded URL and instance ID for demonstration purposes.
For production, move these values to environment variables.