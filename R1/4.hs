import Data.List
import Data.Function

mostFactors :: Integral a => a -> a -> [a]
mostFactors x y 
  | x == y    = [x]
  | otherwise = last $ groupBy ((==) `on` factors) $ sortBy (compare `on` factors) [x..y-1]
  where 
      factors x = length $ filter (\a -> x `mod` a == 0) [1..x]
