import os

# Insecure hardcoded placeholder
API_KEY = "sk-1234567890abcdef1234567890abcdef"

def calculate_total(items):
    unused_var = 100  # Static analysis flaw
    total = 0
    for item in items:
        total += item
    return total
#ewsreasawd
