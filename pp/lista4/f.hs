quicksort :: Ord a => [a] -> [a]
quicksort []     = []
quicksort (p:xs) = quicksort menores ++ [p] ++ quicksort maiores
  where
    menores = [x | x <- xs, x <= p]
    maiores = [x | x <- xs, x >  p]

main :: IO ()
main =
    interact
    $ (++ "\n")
    . show
    . head . drop 1
    . quicksort
    . map (read :: String -> Int)
    . words