import pandas as pd 

def load_and_inspect_data(filepath):
    df = pd.read_csv(filepath, encoding="latin1")
    clean_df = df.copy()

    print("\nDataset Info:")
    clean_df.info()

    print("\n Dataset Shape:", clean_df.shape)

    print("\n Unique Values Per Column:")
    for col in clean_df.columns:
        print(f"{col}: {clean_df[col].nunique()} unique values")

    print("\n Duplicated Rows:", clean_df.duplicated().sum())
    print("\n Missing Values:")
    print(clean_df.isnull().sum())

    print("\n Column Names:")
    print(list(clean_df.columns))

    return df, clean_df


import pandas as pd

def clean_aviation_data(clean_df):
    """
    Cleans and normalizes the aviation dataset.
    
    Steps performed:
    - Drops irrelevant columns
    - Standardizes 'Make' column
    - Fills missing values
    - Fixes inconsistent categorical labels
    - Filters by date (>= 1982)
    - Converts 'Event.Date' to datetime
    - Adds 'Year', 'Month', and 'Total.Injuries' columns

    Returns:
        Cleaned DataFrame
    """

    # Dropping unnecessary columns
    columns_to_drop = [
        'Latitude', 'Longitude', 'FAR.Description', 'Air.carrier',
        'Aircraft.Category', 'Airport.Code', 'Airport.Name',
        'Number.of.Engines', 'Registration.Number', 'Report.Status',
        'Publication.Date', 'Schedule'
    ]
    clean_df.drop(columns=columns_to_drop, axis=1, inplace=True, errors='ignore')

    # Clean 'Make' column
    clean_df['Make'] = clean_df['Make'].str.title().str.strip()

    # Fill numeric injury columns with 0
    numeric_cols = [
        'Total.Fatal.Injuries', 'Total.Serious.Injuries',
        'Total.Minor.Injuries', 'Total.Uninjured'
    ]
    for col in numeric_cols:
        clean_df[col].fillna(0, inplace=True)

    # Fill categorical columns with 'Unknown' or mode
    unknown_fill_cols = [
        'Broad.phase.of.flight', 'Weather.Condition', 'Aircraft.damage',
        'Engine.Type', 'Purpose.of.flight', 'Amateur.Built',
        'Injury.Severity', 'Location', 'Country'
    ]
    for col in unknown_fill_cols:
        clean_df[col].fillna('Unknown', inplace=True)

    clean_df['Make'].fillna(clean_df['Make'].mode()[0], inplace=True)
    clean_df['Model'].fillna(clean_df['Model'].mode()[0], inplace=True)

    # Fix inconsistent labels
    clean_df['Weather.Condition'].replace({'UNK': 'Unknown', 'Unk': 'Unknown'}, inplace=True)
    clean_df['Engine.Type'].replace({'UNK': 'Unknown', 'None': 'Unknown', 'NONE': 'Unknown'}, inplace=True)

    # Filter out dates before 1982
    clean_df = clean_df[clean_df['Event.Date'] >= '1982-01-01']

    # Convert 'Event.Date' to datetime
    clean_df['Event.Date'] = pd.to_datetime(clean_df['Event.Date'], errors='coerce')

    # Create 'Year' and 'Month'
    clean_df['Year'] = clean_df['Event.Date'].dt.year
    clean_df['Month'] = clean_df['Event.Date'].dt.month_name()

    # Add 'Total.Injuries' column
    clean_df['Total.Injuries'] = (
        clean_df['Total.Fatal.Injuries'] +
        clean_df['Total.Serious.Injuries'] +
        clean_df['Total.Minor.Injuries']
    )

   # Remove 'Unknown' or 'Other' if not meaningful
    clean_df = clean_df[~clean_df['Model'].isin(['Unknown', 'Other'])]
    clean_df = clean_df[~clean_df['Engine.Type'].isin(['Unknown', 'None'])]
    clean_df = clean_df[~clean_df['Weather.Condition'].isin(['Unknown', 'UNK', 'Unk'])]

    return clean_df


