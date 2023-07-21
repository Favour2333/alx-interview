#!/usr/bin/env python3
import sys
def main():
    """Main function."""
    total_size = 0
    status_codes = {}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            ip_address, date, method, status_code, file_size = line.split()
        except ValueError:
            continue
        total_size += int(file_size)
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
        if len(status_codes) % 10 == 0 or sys.stdin.isatty():
            print("File size:", total_size)
            for status_code, number in sorted(status_codes.items()):
                print(status_code, number)
    print("File size:", total_size)
    for status_code, number in sorted(status_codes.items()):
        print(status_code, number)
if __name__ == "__main__":
    main()
