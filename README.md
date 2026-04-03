# Zoho Vault to Proton Pass Converter

A stupidly simple Python script that converts Zoho Vault CSV exports to Proton Pass compatible CSV format.

## Requirements

- **Python 3.6+** (tested with 3.8+)
- **pandas** library

## Installation

### 1. Install Python

**macOS:**
```bash
brew install python3
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install python3
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt update && sudo apt install python3 python3-pip
```

**Windows:**
Download and install from [python.org](https://www.python.org/downloads/).

Verify installation:
```bash
python3 --version
```

### 2. Install pandas

```bash
pip3 install pandas
```

## Usage

### Step 1: Export from Zoho Vault

1. Log in to your Zoho Vault account.
2. Go to **Settings** → **Export Passwords**.
3. Select **CSV** format and download the export file.

### Step 2: Convert the CSV

Run the converter with the input and output file paths:

```bash
python3 vault_converter.py <input_file.csv> <output_file.csv>
```

**Example:**
```bash
python3 vault_converter.py zoho-export.csv proton-pass-import.csv
```

### Step 3: Import to Proton Pass

1. Open Proton Pass.
2. Go to **Settings** → **Import**.
3. Select **Proton Pass** as the target.
4. Upload the converted CSV file.

## Column Mapping

| Zoho Vault Field | Proton Pass Field |
|-------------------|-------------------|
| Password Name     | name              |
| Password URL      | url               |
| email             | username          |
| password          | password          |
| Notes             | note              |
| TOTP              | totp              |
| Folder Name       | vault             |

## Extending for Other Password Managers

The script uses `pandas` DataFrames, making it easy to adapt for other formats. Simply:

1. Modify the column mapping in `vault_converter.py`.
2. Update the `protonpass_df` columns to match your target format.

## Troubleshooting

**Error: "Module not found"**
- Run `pip3 install pandas` again to ensure pandas is installed.

**Empty output file**
- Check that your Zoho export uses the column names shown in `zoho-columns.csv`.

**Import fails in Proton Pass**
- Ensure the CSV uses UTF-8 encoding.
- Verify all required fields are present in the output.
