pecas :: Integer -> Integer
pecas n = div ((n + 1) * (n + 2)) 2

main :: IO ()
main = do
    line <- getLine
    let n = read line
    print . pecas $ n