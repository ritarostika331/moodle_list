import argparse

def filter_lines(input_file, output_file, keywords, encoding='utf-8'):
    with open(input_file, 'r', encoding=encoding, errors='ignore') as infile, open(output_file, 'w', encoding=encoding) as outfile:
        for line in infile:
            if any(keyword in line for keyword in keywords):
                outfile.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Filter lines in a file containing specific keywords.')
    parser.add_argument('input_file', help='The input file to read lines from.')
    parser.add_argument('output_file', help='The output file to write filtered lines to.')
    parser.add_argument('keywords', nargs='+', help='List of keywords to filter lines by.')

    args = parser.parse_args()
    
    filter_lines(args.input_file, args.output_file, args.keywords)
