'''
To test if a string is a palindrome, we'll use a two pointer approach that starts at the ends of the string. 
At each step, if the characters at the two pointers are equal, then we'll move both pointers inwards and compare the next set of characters. 
Since a palindrome reads the same forwards and backwards, each pair of characters should be equal at each step.

However, for this problem, we also need to ignore non-alphanumeric characters and ignore case. To do this, we'll use two Python string methods:

The .isalnum() method returns true if a string is alphanumeric, and returns false otherwise. 
The .lower() method converts the entire string into lowercase characters and returns the result.

So inside of the while loop, we check if the characters at index left and right are alphanumeric. 
If they are not, then we skip that character by moving that pointer inwards. 
Once both characters are alphanumeric, we convert both characters to lowercase and check for equality.

If both characters are equal to each other, then we can move on to the next set of characters by moving both pointers inwards. 
If, at this point, they are not equal to each other, then that means that the string is not a palindrome, so we go into the else block and just return false immediately.
'''
def isPalindrome(self, s):          #You should ignore the self parameter if you do not refer to any class instances guys, remember that.
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
'''
Complexities:
Time Complexity: O(n)
In the worst case, every character in the string may need to be checked once, 
either by skipping over non-alphanumeric characters or by comparing two characters at a time. 
This results in the loop running in O(n) time, where n is the length of the string.

Space Complexity : O(1)
No extra space used.
'''
