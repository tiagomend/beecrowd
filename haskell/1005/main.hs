import Text.Printf (printf)

averageOne :: IO String
averageOne = do
    a <- readLn :: IO Double
    b <- readLn :: IO Double

    let weightOfA = 3.5
        weightOfB = 7.5

    let media = (a * weightOfA + b * weightOfB) / (weightOfA + weightOfB)

    return $ printf "MEDIA = %.5f" media

main :: IO ()
main = do
    result <- averageOne
    putStrLn result