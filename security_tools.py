# Security Tools Module
# IT420 Project - Group 5
# Contains business logic for password and email breach checking

import hashlib
import requests
from typing import Optional, List


def check_password_hibp(password: str) -> Optional[int]:
    """
    Check if a password is compromised using Have I Been Pwned API with k-anonymity.
    
    Args:
        password (str): The password to check
        
    Returns:
        Optional[int]: Number of breaches found, 0 if safe, None if error
    """
    # 1. Hash the password (SHA-1)
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1[:5]   # First 5 chars for the API
    suffix = sha1[5:]   # The rest is kept secret locally

    # 2. Query the API with ONLY the prefix
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        resp = requests.get(url, headers={"User-Agent": "SecureCheck-App"}, timeout=5)
        if resp.status_code != 200:
            return None
        
        # 3. Search the response LOCALLY for the suffix
        # The API sends back a list of suffixes (hashes sharing the same prefix)
        hashes = (line.split(':') for line in resp.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)  # Match found!
        return 0  # No match found
    except Exception:
        return None


def check_email_xon(email: str) -> Optional[List[str]]:
    """
    Check if an email is compromised using XposedOrNot API.
    
    Args:
        email (str): The email address to check
        
    Returns:
        Optional[List[str]]: List of breach names if found, empty list if safe, None if error
    """
    url = f"https://api.xposedornot.com/v1/check-email/{email}"
    try:
        resp = requests.get(url, headers={"User-Agent": "SecureCheck-App"}, timeout=5)
        if resp.status_code != 200:
            return None
        
        data = resp.json()
        if "Error" in data:  # API returns "Error" key if no breaches found
            return []
        
        # Structure: {"breaches": [...]}
        return data.get("breaches", []) if data.get("breaches") else []
    except Exception:
        return None