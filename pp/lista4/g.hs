solve :: [Int] -> Int
solve (x:n:xs) = x * (n + 1) - sum xs

main :: IO ()
main = 
    interact
    $ (++ "\n")
    . show
    . solve
    . map read
    . words