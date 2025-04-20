import pandas as pd
import sys,os

def clean_dataset(file_path):
    
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    hp = pd.read_csv(file_path)
    
    print(len(hp))
    print(hp.dtypes)
    
    #format columns
    # Strip extra whitespace from strings
    # Could also go further and convert everything to lowercase, collapse extra internal spaces, etc...
    string_columns = hp.select_dtypes(["object"])
    hp[string_columns.columns] = string_columns.apply(lambda x: x.str.strip())
    hp['bathrooms'] = hp['bathrooms'].round()
    
    #Renaming Columns for better Understanding
    hp.columns = [col.upper() for col in hp.columns]
    hp.columns = ["DATE","NUM_OF_BEDROOMS","NUM_OF_BATHROOMS","LIVING_AREA_sqft","LOT_AREA_sqft", "FLOORS","WATER FRONT","VIEW_RATING","CONDITION_RATING", "ABOVE_BASEMENT_sqft", "BASEMENT_sqft", "YEAR_BUILT", "YEAR_RENOVATED","STREET","CITYZIP ","STATE","COUNTRY","PRICE"]
    
    #Typecasting
    pd.options.display.float_format = '{:,.1f}'.format
    hp.PRICE = hp.PRICE.astype(float)
    # Turn date string into an actual date object
    hp["DATE"] = pd.to_datetime(hp["DATE"])

    #Dictionary Mapping
    word_to_num = {'one': 1, 'two': 2, 'three': 3}
    hp['FLOORS'] = hp['FLOORS'].replace(word_to_num)
    hp['FLOORS'] = hp['FLOORS'].astype(float)
    hp.dtypes

    #Deleting Duplicate Rows
    duplicate_rows = hp[hp.duplicated()]
    hp.drop_duplicates(inplace=True)
    duplicate_rows

    #Column Splitting
    # Split 'cityzip' into 'city' and 'zip' columns
    hp[['CITY', 'ZIP']] = hp.iloc[:, -4].str.split(' ', expand=True)
    # Drop the original 'cityzip' column if needed
    # hp.drop('cityzip', axis=1, inplace=True)
    
    #Filling Null Values
    # Fill null values in 'NUM_OF_BEDROOMS' with the mode
    mode_NUM_OF_BEDROOMS = hp['NUM_OF_BEDROOMS'].mode()[0]  # Calculates the mode
    hp['NUM_OF_BEDROOMS'] = hp['NUM_OF_BEDROOMS'].fillna(mode_NUM_OF_BEDROOMS)

    # Fill null values in 'NUM_OF_BATHROOMS' with the mode
    mode_NUM_OF_BATHROOMS = hp['NUM_OF_BATHROOMS'].mode()[0]  # Calculate the mode
    hp['NUM_OF_BATHROOMS'] = hp['NUM_OF_BATHROOMS'].fillna(mode_NUM_OF_BATHROOMS)

    # Fill null values in 'NUM_OF_BEDROOMS' with the mode
    mode_FLOORS = hp['FLOORS'].mode()[0]  # Calculates the mode
    hp['FLOORS'] = hp['FLOORS'].fillna(mode_FLOORS)

    # Fill null values in 'NUM_OF_BEDROOMS' with the mode
    mode_WATERFRONT = hp['WATER FRONT'].mode()[0]  # Calculates the mode
    hp['WATER FRONT'] = hp['WATER FRONT'].fillna(mode_WATERFRONT)

    # Fill null values in 'NUM_OF_BEDROOMS' with the mode
    mode_VIEW_RATING = hp['VIEW_RATING'].mode()[0]  # Calculates the mode
    hp['VIEW_RATING'] = hp['VIEW_RATING'].fillna(mode_VIEW_RATING)

    # Fill null values in 'NUM_OF_BEDROOMS' with the mode
    mode_CONDITION_RATING  = hp['CONDITION_RATING'].mode()[0]  # Calculates the mode
    hp['CONDITION_RATING'] = hp['CONDITION_RATING'].fillna(mode_NUM_OF_BEDROOMS)

    #Feature Engineering
    # Add a new feature for the total square feet
    hp["TOTAL_HOUSE_AREA_sqft"] = hp["ABOVE_BASEMENT_sqft"] + hp["BASEMENT_sqft"]
    hp.describe()

    #Invalid Column Correction
    invalid_rows = hp[(hp['YEAR_BUILT'] > hp['YEAR_RENOVATED']) & (hp['YEAR_RENOVATED'] != 0)]
    invalid_rows

    hp.drop(invalid_rows.index, inplace=True)
    hp

    #Invalid Data Cleaning
    # Based on the above summary data (and prior EDA!!!), we should get rid of some missing/invalid data
    hp = hp[hp["NUM_OF_BEDROOMS"] != ""]
    hp = hp[hp["NUM_OF_BATHROOMS"] != ""]
    hp = hp[hp["LIVING_AREA_sqft"] > 0]
    hp = hp[hp["LOT_AREA_sqft"] > 0]
    hp = hp[hp["FLOORS"] > 0]
    hp = hp[hp["TOTAL_HOUSE_AREA_sqft"] > 0]
    hp = hp[hp["VIEW_RATING"] >= 0]
    hp = hp[hp["CONDITION_RATING"] >= 0]
    hp = hp[hp["YEAR_BUILT"] > 1900]
    hp = hp[hp["PRICE"] > 10000]

    #dropping columns
    hp = hp.drop(columns = ['DATE','COUNTRY','STREET','STATE'])
    # Assuming 'index_to_drop' is the index of the column you want to drop
    hp.drop(hp.columns[-5], axis=1, inplace=True)
    
    q1=hp['PRICE'].quantile(0.25)
    q3=hp['PRICE'].quantile(0.75)
    iqr=q3-q1
    upper_limit=q3+(1.5*iqr)
    lower_limit=q1-(1.5*iqr)
    upper_limit,lower_limit
    hp.loc[(hp['PRICE']>upper_limit) | (hp['PRICE']<lower_limit) ]
    hp=hp.loc[(hp['PRICE']<upper_limit) & (hp['PRICE']>lower_limit)]

    q1=hp['LOT_AREA_sqft'].quantile(0.25)
    q3=hp['LOT_AREA_sqft'].quantile(0.75)
    iqr=q3-q1
    upper_limit=q3+(1.5*iqr)
    lower_limit=q1-(1.5*iqr)
    upper_limit,lower_limit
    hp.loc[(hp['LOT_AREA_sqft']>upper_limit) | (hp['LOT_AREA_sqft']<lower_limit) ]
    hp=hp.loc[(hp['LOT_AREA_sqft']<upper_limit) & (hp['LOT_AREA_sqft']>lower_limit)]
         
    cleaned_file_path = 'cleaned_housing_dataset.csv'
    hp.to_csv(cleaned_file_path, index=False)

    return cleaned_file_path

if __name__ == '__main__':
    # Check if the file path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python clean_dataset.py <file_path>")
        sys.exit(1)

    # Get the file path from the command-line arguments
    file_path = sys.argv[1]

    # Call the clean_dataset function with the provided file path
    cleaned_file_path = clean_dataset(file_path)
    print(f"Dataset cleaned successfully. Cleaned file saved as: {cleaned_file_path}")