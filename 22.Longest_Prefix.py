# Write a program to find the longest common prefix in an array of strings

def longest_prefix(strings):
    if not strings:
        return ""
    
    prefix = strings[0]

    for string in strings[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]

            if not prefix:
                return ""
            
    return prefix

strings = ["flaw","flight","flew","flow","flag"]
print(longest_prefix(strings))