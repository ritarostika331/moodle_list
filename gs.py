# Function to process the URLs and login information
def process_urls_and_login_info(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Strip any extra whitespace characters
            line = line.strip()
            
            # Split the line into its components
            components = line.split('|')
            
            # Check if the URL starts with 'http://', 'https://', or 'www.'
            if not components[0].startswith(('http://', 'https://', 'www.')):
                # Add 'http://' if it's missing
                components[0] = 'http://' + components[0]
            
            # Join the components back into a single line
            processed_line = '|'.join(components)
            
            # Write the processed line to the output file
            outfile.write(processed_line + '\n')

# Specify the input and output file names
input_file = 'mk.txt'
output_file = 'processed_urls.txt'

# Call the function to process the URLs and login information
process_urls_and_login_info(input_file, output_file)

print(f'Processed URLs and login information have been saved to {output_file}')
