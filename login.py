import logging
import yaml
import pyotp
from NorenRestApiPy.NorenApi import NorenApi

# ------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S"
)


# ------------------------------------------------------------
# Shoonya API Wrapper Class
# ------------------------------------------------------------
class ShoonyaApiPy(NorenApi):
    """Custom wrapper for Shoonya Noren API"""
    
    def __init__(self):
        super().__init__(
            host='https://api.shoonya.com/NorenWClientTP/',
            websocket='wss://api.shoonya.com/NorenWSTP/'
        )
        logging.info("Shoonya API initialized.")


# ------------------------------------------------------------
# Helper: Load credentials safely
# ------------------------------------------------------------
def load_credentials(file_path='cred.yml'):
    """Load user credentials from YAML file."""
    try:
        with open(file_path, 'r') as f:
            creds = yaml.safe_load(f)
        required_keys = ['user', 'pwd', 'vc', 'apikey', 'imei', 'token']
        for key in required_keys:
            if key not in creds:
                raise KeyError(f"Missing key: {key}")
        return creds
    except FileNotFoundError:
        logging.error(f"Credential file '{file_path}' not found.")
        exit(1)
    except Exception as e:
        logging.error(f"Error loading credentials: {e}")
        exit(1)


# ------------------------------------------------------------
# Main Execution
# ------------------------------------------------------------
def main():
    creds = load_credentials()

    # Generate 2FA OTP dynamically
    otp = pyotp.TOTP(creds['token']).now()

    # Create API object
    api = ShoonyaApiPy()

    # Perform login
    logging.info("Attempting to log in to Shoonya...")
    ret = api.login(
        userid=creds['user'],
        password=creds['pwd'],
        twoFA=otp,
        vendor_code=creds['vc'],
        api_secret=creds['apikey'],
        imei=creds['imei']
    )

    # Validate login
    if ret and ret.get('stat') == 'Ok':
        logging.info(f"[✅] Login successful: {creds['user']}")
    else:
        logging.error("[❌] Login failed. Check credentials or network.")
        logging.debug(f"Response: {ret}")

    return api


# ------------------------------------------------------------
# Script Entry Point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
