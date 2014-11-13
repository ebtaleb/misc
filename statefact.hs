{-# LANGUAGE NoMonomorphismRestriction #-}

import Control.Monad.State

statefulFactorial = do
    (x, y) <- get
    if y == 0 then
        return x
    else
        do
        put (x*y, y-1)
        statefulFactorial

runStatefulFactorial n = fst (runState statefulFactorial (1, n))
