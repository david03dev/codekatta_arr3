def remove_duplicates(passport_list):
    # Convert the list to a set to remove duplicates
    unique_passports = set(passport_list)
    
    # Convert the set back to a list to maintain order (optional, as per requirement)
    unique_passport_list = list(unique_passports)
    
    # Join the list into a single string separated by spaces
    result = ' '.join(unique_passport_list)
    
    return result

# Reading input
n = int(input())  # Read the number of passport numbers (not used explicitly)
passports = input().split()  # Read the list of passport numbers

# Remove duplicates
result = remove_duplicates(passports)

# Print the result
print(result)
