import pandas as pd

# Function to filter the data
def filter_data(csv_file, output_file):
    """
    Filter permitting data for properties with a specified minimum number of units and save it to a new CSV file.

    Args:
        csv_file (str): Path to the input CSV file.
        output_file (str): Path for the output CSV file.

    Returns:
        None
    """
    try:
        # Load the ZBA CSV file into a DataFrame
        df = pd.read_csv(csv_file)

        # Prompt the user for the minimum number of units
        min_units = int(input("Enter the minimum number of units to filter: "))

        # Filter the DataFrame for properties with the specified minimum units
        filtered_df = df[df['Number of Units'] >= min_units]

        if not filtered_df.empty:
            # Save the filtered data to a new CSV file
            filtered_df.to_csv(output_file, index=False)
            print(f"Filtered data with {min_units}+ units saved to {output_file}")
        else:
            print(f"No properties with {min_units}+ units found in the dataset.")

    except FileNotFoundError:
        print(f"Error: The file {csv_file} not found.")
    except ValueError:
        print("Error: Please enter a valid integer for the minimum number of units.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Specify the input and output filenames
input_csv_file = "path_to_your_input_csv_file.csv"
output_csv_file = "path_to_your_output_csv_file.csv"

# Call the function to filter and save the data
filter_data(input_csv_file, output_csv_file)
