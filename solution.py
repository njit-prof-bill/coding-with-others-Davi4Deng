def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    char_count = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        if len(char_count) == k:
            max_length = max(max_length, right - left + 1)

    return max_length
s1 = "araaci"
k1 = 2
s2 = "cbbebi"
k2 = 3
s3 = "aa"
k3 = 1
print(longest_substring_k_unique(s1, k1))
print(longest_substring_k_unique(s2, k2))
print(longest_substring_k_unique(s3, k3))   
