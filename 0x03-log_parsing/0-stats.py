#!/usr/bin/python3
import sys

def print_metrics(total_file_size, status_codes):
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_codes):
        print("{}: {}".format(status_code, status_codes[status_code]))

def main():
    total_file_size = 0
    status_codes = {}

    try:
        for idx, line in enumerate(sys.stdin, 1):
            data = line.split()

            # Check if the line matches the input format
            if len(data) != 9 or not data[8].isdigit():
                continue

            file_size = int(data[8])
            total_file_size += file_size

            status_code = data[7]
            if status_code in ['200', '301', '400', '401', '403', '404', '405', '500']:
                status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if idx % 10 == 0:
                print_metrics(total_file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_codes)
        sys.exit(0)

if __name__ == "__main__":
    main()

