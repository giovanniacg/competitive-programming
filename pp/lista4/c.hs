main :: IO ()
main = 
    interact $ (++ "\n") . show . subtract 3 . sum . map read . words