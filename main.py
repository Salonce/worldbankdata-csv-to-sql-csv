import sys

if len(sys.argv) != 3:
    print("Error. Usage: python script.py input_filename output_filename")
    sys.exit(1)

#input_filename = "gdp_data.csv"
#output_filename = "gdp_data_sql.csv"

input_folder = 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\'
output_folder = 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\'

input_filename = sys.argv[1]
output_filename = sys.argv[2]

with open(input_folder + input_filename, 'r') as file:
    lines = file.readlines()

# Process each line
processed_lines = []
for line in lines:
    # Remove trailing comma if present
    if line[-2] == ',':
        line = line[:-2] + line[-1]
    if line[-1] == ',':
        line = line[:-1]

    # Replace doubled double quotes with 'NULL'
    line = line.replace('""', 'NULL')

    # Append processed line to the list
    processed_lines.append(line)

# Join processed lines into a single string
processed_data = ''.join(processed_lines)

# Save the modified string to a new CSV file
print(processed_data);
with open(output_folder + output_filename, 'w') as new_file:
    new_file.write(processed_data)