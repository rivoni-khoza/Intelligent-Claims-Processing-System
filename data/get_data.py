# get_data.

import requests
import pandas as pd
from typing import Dict

def load_claim_data(url: str, params: Dict[str, str]) -> pd.DataFrame:
    """
    Loads claim data from a given SODA API endpoint.

    Args:
        url (str): The API endpoint URL.
        params (Dict[str, str]): Query parameters to pass with the request.

    Returns:
        pd.DataFrame: A DataFrame containing the claim data.
    """
    response = requests.get(url, params=params)
    response.raise_for_status()
    return pd.DataFrame(response.json())

def 