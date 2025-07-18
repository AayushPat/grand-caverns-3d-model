import csv

# Define the input and output file names
input_file = 'lidar_data.txt'
output_file = 'data3.csv'

# Define the subsampling factor (e.g., 2 for every 2nd point, 5 for every 5th point, etc.)
subsample_factor = 1  # Change this to your desired subsampling rate

# Initialize variables to store min and max X, Y, and Z values
min_x = float('inf')
min_y = float('inf')
min_z = float('inf')
max_x = float('-inf')
max_y = float('-inf')
max_z = float('-inf')
max_intense = float('-inf')

# Open the input text file and the output CSV file
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    # Create a CSV writer object
    csv_writer = csv.writer(outfile)
    
    # Write the header row to the CSV file (now with Intensity)
    csv_writer.writerow(['X', 'Y', 'Z', 'Intensity'])
    
    # Read each line from the input file
    for line_number, line in enumerate(infile, start=1):
        # Strip whitespace and skip empty lines
        line = line.strip()
        if not line:
            print(f"Warning: Line {line_number} is empty and will be skipped.")
            continue
        
        # Split the line into components
        parts = line.split()
        
        # Check if the line has at least 4 columns (now checking for Intensity)
        if len(parts) < 4:
            print(f"Warning: Line {line_number} has fewer than 4 columns and will be skipped.")
            continue
        
        try:
            # Extract the X, Y, Z, and Intensity values (first four columns)
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            intensity = float(parts[3])  # New: Extract intensity
            
            # Update min and max X, Y, and Z values (unchanged)
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
            if z < min_z:
                min_z = z
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            if z > max_z:
                max_z = z
            if intensity > max_intense:
                max_intense = intensity
            
            # Subsample: Only write every n-th point (where n = subsample_factor)
            if line_number % subsample_factor == 0:
                csv_writer.writerow([x, y, z, intensity])  # Now including intensity
        except ValueError as e:
            print(f"Warning: Line {line_number} contains invalid data and will be skipped. Error: {e}")

# Print the minimum and maximum X, Y, and Z values
print(f"Min X: {min_x}")
print(f"Min Y: {min_y}")
print(f"Min Z: {min_z}")
print(f"Max X: {max_x}")
print(f"Max Y: {max_y}")
print(f"Max Z: {max_z}")
print(f"Max I: {max_intense}")


print(f"Data has been successfully written to {output_file}")