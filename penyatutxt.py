import os

# Fungsi untuk menulis semua baris ke result.txt satu per satu
def write_result_file():
    with open('result.txt', 'w') as result_file:
        for filename in os.listdir('.'):
            if filename.endswith('.txt') and filename != 'result.txt':
                with open(filename, 'r', errors='ignore') as file:  # Menambahkan errors='ignore'
                    for line in file:
                        result_file.write(line)

# Main
if __name__ == "__main__":
    write_result_file()
    print("Semua baris telah disatukan ke dalam result.txt")
