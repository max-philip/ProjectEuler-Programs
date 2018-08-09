-- Problem 28
-- Number Spiral Diagonals
-- Starting with the number 1 and moving to the right in a clockwise direction a
-- 5 by 5 spiral is formed as follows:

-- 21 22 23 24 25
-- 20  7  8  9 10
-- 19  6  1  2 11
-- 18  5  4  3 12
-- 17 16 15 14 13
--
-- It can be verified that the sum of the numbers on the diagonals is 101.
--
-- What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
-- formed in the same way?


-- get list of Diagonals
diags :: Int -> [Int]
diags 1 = [1]
diags n = (take (((n-1)`div`2)*4) [2,4..])

spiral_sum :: Int -> Int
spiral_sum 0 = 0
spiral_sum 1 = 1
spiral_sum n = (sum (diags n)) + (spiral_sum (n-2)) + 4
