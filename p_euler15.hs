-- Problem 15
-- Lattice Paths

module Main where

main :: IO ()
main = return ()


paths :: Integer -> Integer -> Integer
paths n 0 = 1
paths 0 m = 1
paths n m = (paths n (m-1)) + (paths (n-1) m)



-- => (m+n-2) CHOOSE (n-1)

-- m x n grid:
-- need m UPs and n RIGHTs.
-- whatever path you take, you end up with the same number of
-- UPs and RIGHTs.
-- e.g. UURR and URUR are valid paths
-- => you know the sequence length is (m + n - 2)
