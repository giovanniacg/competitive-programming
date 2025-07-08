solve :: [Int] -> (Int, Int)
solve (_:xs) = (min i1 (i1 - i2), i2)
    where
        xs1 = [x | x <- xs, x == 1]
        xs2 = [x | x <- xs, x == 2]
        i1 = mod (length xs1) 2
        i2 = mod (length xs2) 2

main :: IO ()
main = 
    interact
    $ (++ "\n")
    . show
    . map (++ "\n")
    . solve
    . map read 
    . words