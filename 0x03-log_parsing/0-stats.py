#!/usr/bin/python3

import sys
import signal

# Initialize variables
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0

def print_statistics():
    """Print the computed statistics"""
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts):
        if status_code_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_code_counts[status_code]))

def signal_handler(signal, frame):
    """Handle the keyboard interruption (CTRL + C)"""
    print_statistics()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Process input line by line
for line in sys.stdin:
    # Parse the line
    try:
        parts = line.split()
        ip_address = parts[0]
        date = parts[3][1:-1]  # Corrected the date extraction
        status_code = int(parts[8])
        file_size = int(parts[9])
    except IndexError:
        continue
    except (ValueError, IndexError):
        continue

    # Update the metrics
    total_file_size += file_size
    status_code_counts[status_code] += 1
    lines_processed += 1

    # Print statistics every 10 lines
    if lines_processed % 10 == 0:
        print_statistics()

# Print the final statistics
print_statistics()

