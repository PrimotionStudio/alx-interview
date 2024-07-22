#!/usr/bin/env python3
"""
This module contains the function
"""
import sys
import signal
from typing import Dict, List


total_file_size: int = 0
status_code_counts: Dict[int, int] = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count: int = 0


def print_stats():
    """Print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handle the SIGINT signal (Ctrl+C)."""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    parts: List[str] = line.split()
    
    if len(parts) != 9 or parts[2] != 'GET':
        continue
    
    try:
        status_code: int = int(parts[-2])
        file_size: int = int(parts[-1])
    except ValueError:
        continue
    
    total_file_size += file_size
    
    if status_code in status_code_counts:
        status_code_counts[status_code] += 1
    
    line_count += 1
    
    if line_count % 10 == 0:
        print_stats()

print_stats()
