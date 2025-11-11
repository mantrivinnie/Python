# Program to find the Longest Common Subsequence (LCS) between two strings

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Create a 2D array to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from dp table
    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str = X[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_str


# Example usage
X = input("Enter first string: ")
Y = input("Enter second string: ")

result = lcs(X, Y)
print(f"\nLongest Common Subsequence: {result}")
print(f"Length of LCS: {len(result)}")



#Enter first string: ABCDGH
#Enter second string: AEDFHR

#Longest Common Subsequence: ADH
#Length of LCS: 3
