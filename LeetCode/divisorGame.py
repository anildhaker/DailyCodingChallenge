# Alice and Bob take turns playing a game, with Alice starting first.

# Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

# Choosing any x with 0 < x < N and N % x == 0.
# Replacing the number N on the chalkboard with N - x.


def divisorGame(self, N: int) -> bool:
        if N <= 1:
            return False
        
        
        dp = [False for i in range(N+1)]
        
        for i in range(2,N+1):
            for j in range(1,i//2+1):
                if i % j == 0: # choosing x = j
                    newN = i - j
                    if dp[newN] == False:
                        dp[i] = True
                        
        return dp[N]
        