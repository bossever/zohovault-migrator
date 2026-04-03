
import pandas as pd
import sys

def convert_zoho_to_protonpass(input_file, output_file):
    """
    Converts a Zoho Vault CSV export to a Proton Pass compatible CSV file.

    Args:
        input_file (str): The path to the Zoho Vault CSV file.
        output_file (str): The path to save the Proton Pass compatible CSV file.
    """
    try:
        # Read the Zoho Vault CSV file
        zoho_df = pd.read_csv(input_file)

        # Create a new DataFrame for the Proton Pass format
        protonpass_df = pd.DataFrame()

        # Map the columns
        protonpass_df['name'] = zoho_df.get('Password Name', '')
        protonpass_df['url'] = zoho_df.get('Password URL', '')
        protonpass_df['email'] = ''
        protonpass_df['username'] = zoho_df.get('email', '')
        protonpass_df['password'] = zoho_df.get('password', '')
        protonpass_df['note'] = zoho_df.get('Notes', '')
        protonpass_df['totp'] = zoho_df.get('TOTP', '')
        protonpass_df['vault'] = zoho_df.get('Folder Name', '')

        # Save the new DataFrame to a CSV file
        protonpass_df.to_csv(output_file, index=False)
        print(f"Successfully converted '{input_file}' to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python vault_converter.py <input_file> <output_file>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    convert_zoho_to_protonpass(input_csv, output_csv)
