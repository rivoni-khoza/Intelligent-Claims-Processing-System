import pandas as pd
import re

def clean_claim_data(df: pd.DataFrame, null_threshold: float = 0.5) -> pd.DataFrame:
    """
    Cleans the claims dataset:
    - Drops columns with > null_threshold missing values
    - Standardizes all string columns
    - Optionally cleans claim descriptions

    Parameters:
        df (pd.DataFrame): Raw claims DataFrame
        null_threshold (float): Proportion of allowed missing values (default = 0.5)

    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    df = df.copy()

    # --- Drop columns with >50% nulls ---
    null_ratio = df.isnull().mean()
    high_null_cols = null_ratio[null_ratio > null_threshold].index.tolist()
    df.drop(columns=high_null_cols, inplace=True)

    # --- Standardize all string/categorical columns ---
    obj_cols = df.select_dtypes(include='object').columns

    for col in obj_cols:
        df[col] = df[col].astype(str).str.strip().str.lower().str.replace('_', ' ', regex=False)

    # --- Clean 'claim_description' if present ---
    if 'claim_description' in df.columns:
        df['claim_description_clean'] = (
            df['claim_description']
            .astype(str)
            .str.lower()
            .apply(lambda x: re.sub(r'[^a-z0-9\s]', '', x))
        )

    # --- Drop rows with missing accident_date ---
    if 'accident_date' in df.columns:
        df = df.dropna(subset=['accident_date'])
        df['accident_date'] = pd.to_datetime(df['accident_date'], errors='coerce')

    return df



def add_claim_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds engineered features: age_group, accident_month.
    Ensures age_at_injury is numeric and drops invalid entries.
    """
    import pandas as pd
    df = df.copy()

    # Ensure accident_date is datetime
    if not pd.api.types.is_datetime64_any_dtype(df['accident_date']):
        df['accident_date'] = pd.to_datetime(df['accident_date'], errors='coerce')

    # Accident month
    df['accident_month'] = pd.Categorical(
        df['accident_date'].dt.month_name(),
        categories=[
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ],
        ordered=True
    )

    # Clean age column
    df['age_at_injury'] = (
        df['age_at_injury']
        .astype(str)
        .str.strip()
        .replace('', pd.NA)
    )
    
    # Coerce to numeric
    df['age_at_injury'] = pd.to_numeric(df['age_at_injury'], errors='coerce')

    # Drop invalid age rows
    df = df.dropna(subset=['age_at_injury'])

    # Binning ages
    bins = [0, 18, 30, 45, 60, 75, 100]
    labels = ['<18', '18–29', '30–44', '45–59', '60–74', '75+']
    df['age_group'] = pd.cut(df['age_at_injury'], bins=bins, labels=labels, right=False)

    return df



