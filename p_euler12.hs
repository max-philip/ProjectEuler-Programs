-- Problem 12
-- Highly Divisible Triangular Number

module Main where

main :: IO ()
main = return ()


tri_num :: Int -> Int
tri_num 1 = 1
tri_num n = sum [1..n]


factors :: Int -> [Int]
factors 0 = []
factors 1 = [1]
factors n = [f | f <- [1..n], n `mod` f == 0]


first_div :: [Int] -> Int -> Int
first_div [] 0 = 0
first_div (x:xs) y
    | length (factors x) >= y    = x
    | otherwise                 = first_div xs y
