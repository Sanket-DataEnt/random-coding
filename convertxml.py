import os
import pandas as pd

def read_xml_files_to_dataframe(folder_path):
    """
    Reads all XML files in the specified folder and appends them into a single DataFrame.

    Parameters:
    folder_path (str): The path to the folder containing XML files.

    Returns:
    pd.DataFrame: A DataFrame containing the combined data from all XML files.
    """
    # Initialize an empty list to store DataFrames
    dataframes = []

    # Iterate over all files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(folder_path, filename)
            try:
                # Read the XML file into a DataFrame
                df = pd.read_xml(file_path)
                # Append the DataFrame to the list
                dataframes.append(df)
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(dataframes, ignore_index=True)

    return combined_df

# Example usage
folder_path = 'data'  # Replace with your folder path
combined_dataframe = read_xml_files_to_dataframe(folder_path)

# Display the combined DataFrame
print(combined_dataframe)

combined_dataframe.to_csv('output/combined_data.csv', index=False)