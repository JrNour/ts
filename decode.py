import base58
import codecs

def raw_to_private_key(raw_data):
    try:
        # Attempt to decode as if it's a WIF key
        decoded = base58.b58decode(raw_data)
        is_compressed = decoded[-5] == 0x01
        private_key_full = decoded[1:-4]  # Strip off version byte and checksum
        if is_compressed:
            private_key_full = private_key_full[:-1]  # Strip off compression flag
    except Exception as e:
        # If it fails, just treat the raw data as hex
        private_key_full = bytes.fromhex(raw_data)
    
    private_key_hex = codecs.encode(private_key_full, 'hex')
    return private_key_hex

def process_data(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            raw_data = line.strip()
            if raw_data:
                try:
                    private_key = raw_to_private_key(raw_data)
                    outfile.write(f"{private_key.decode()}\n")
                except Exception as e:
                    print(f"Error processing {raw_data}: {e}")

# Define input and output file paths
input_file_path = 'modified_output.txt'  # Replace with your input file name
output_file_path = 'pri.txt'  # Replace with your output file name

# Process the input file and write to the output file
process_data(input_file_path, output_file_path)
print(f"Processing completed. Check the output file {output_file_path}.")
