solve :: Int -> Int
solve x =
    if x < 18
    then 15
    else if x < 60
        then 30
        else 20

main :: IO ()
main =
    interact
    $ (++ "\n")
    . show
    . sum
    . map solve
    . map read
    . words
