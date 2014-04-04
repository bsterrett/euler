fibonacci = 0 : 1 : zipWith (+) fibonacci (tail fibonacci)
boundedFibs = [ x | x <- fibonacci, x < 10000000 ]
evenFibs = [ x | x <- fibonacci, rem x 2 == 0, x < 4000000 ]

main = do
  let fibSum = show (sum boundedFibs)
  putStrLn fibSum 


fib' :: Int -> Int
fib' (-1) = 0
fib' 0 = 0
fib' 1 = 1
fib' n = (fib' n-1) + (fib' n-2)
