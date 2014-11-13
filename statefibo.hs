--{-# LANGUAGE NoMonomorphismRestriction #-}

import Control.Monad.State

statefulFibo = do
        (x, y) <- get
        case x of
          1 -> return (x, y)
          _ -> do put (x - 1, (snd y, fst y + snd y))
                  statefulFibo

--let fibStep = do (u,v) <- get; put (v,u+v) in execState (replicateM 7 fibStep) (0,1)
--
fibStep (u, v) = do
    n <- get
    if n == 0 then return (u, v) else do put (n-1)
                                         fibStep (v, u+v)

--let fib (u,v) = do n <- get; if n == 0 then return (u,v) else (do put (n-1); fib (v, u+v)) in runState (fib (0,1)) 10
