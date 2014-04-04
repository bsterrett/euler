divides y x = rem x y == 0

divisibleNums = [ x | x <- [1..999], divides 3 x || divides 5 x ]

main = do
  let printNums = show (sum divisibleNums)
  putStrLn printNums
