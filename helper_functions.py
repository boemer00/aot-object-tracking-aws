def fix_json_commas(file_path, output_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    with open(output_path, 'w') as f_out:
        f_out.write('[\n')  # Start array

        inside_object = False  # Track whether we're inside an object
        first_object = True    # Track the first object to avoid unnecessary commas

        for line in lines:
            stripped_line = line.strip()

            # Detect start of an object
            if stripped_line == '{':
                if not first_object:
                    f_out.write(',\n')  # Add comma before starting a new object, but not for the first object
                first_object = False
                inside_object = True
                f_out.write(line)

            # Detect end of an object
            elif stripped_line == '}':
                inside_object = False
                f_out.write(line)

            # Skip lines that are just commas
            elif stripped_line == ',':
                continue

            # Copy lines within the object directly
            else:
                f_out.write(line)

        f_out.write('\n]')  # End array

# Example file paths
input_file = os.path.join(dataset_folder, 'valid_encounters.json')
output_file = os.path.join(dataset_folder, 'cleaned_valid_encounters.json')

# Run the fix
fix_json_commas(input_file, output_file)

print(f"Fixed JSON file written to: {output_file}")
