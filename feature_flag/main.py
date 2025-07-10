from flask import Flask
from UnleashClient import UnleashClient

app = Flask(__name__)

@app.route('/flag1', methods=["GET"])
def demo_enable():
    if is_enable_flag("demo_flag_enable"):
        return "Flag1 Enabled"
    else:
        return "Flag1 not enabled"

@app.route('/flag2', methods=["GET"])
def demo_disable():
    if is_enable_flag("demo_flag_disable"):
        return "Flag2 Enabled"
    else:
        return "Flag2 not enabled"

def is_enable_flag(flag_name):
    # Hardcoded for demo poc, in prod put it in env
    client = UnleashClient(
        url="https://gitlab.com/api/v4/feature_flags/unleash/71519768",
        app_name="All Environments",
        instance_id="glffct-ycT2X_atMMzmWAeHaxj5"
    )
    client.initialize_client()
    return client.is_enabled(flag_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


    



