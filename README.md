# Bloomberg Challenge
1D Candy Crush 

This coding challenge comes from a Bloomerg interview question posted on leetcode:

https://leetcode.com/discuss/interview-question/380650/Bloomberg-or-Phone-Screen-or-Candy-Crush-1D

To summarize, the goal is to create a function that will remove chunks of 3 or more of the same letter appearing consecutively, resulting in the shortest possible version of the string. For example:

`aaabbbcc` --> `cc` (solution: remove 3 a's, remove 3 b's)

The "hard" version requires a brute-force approach to check all possiblities, for example:

`aaabbbaa` --> ` ` (solution: remove 3 b's, remove 5 a's) — requires waiting to delete the a's until after b's are removed.

Even harder:

`aaabbbcccbacd` --> `cd` (solution: remove 3 c's, remove 4 b's, remove 4 a's)


I accomplished the task using recursion, completing each branch possibility and scoring results to return the shortest possible string. I also built in a parameter to allow the user to choose the minimum contiguous appearances of a letter to "pop" (3 by default).  
