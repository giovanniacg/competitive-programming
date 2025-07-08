main :: IO ()
main =
    interact 
    $ (++ "\n")
    . show
    . (\[e,d] -> 
            if e > d
            then e + d
            else 2 * (d - e)
        )
    . map read
    . words
    