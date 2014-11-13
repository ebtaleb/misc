import qualified Data.ByteString as B
import Network.HTTP
import Text.HTML.TagSoup
import Data.Maybe
import Network.URI (parseURI)

sigh list = do
    pika <- listToMaybe list
    return pika

downloadImg nb = do

    let toget = "http://ck.booru.org/index.php?page=post&s=view&id=" ++ show nb
    http <- simpleHTTP (getRequest toget) >>= getResponseBody
    let tags = dropWhile (~/= TagOpen "img" [("alt", "img")]) (parseTags http)

    let derp = fromJust $ sigh tags
    let imgurl = fromAttrib "src" derp

    let ext = drop (length imgurl - 4) imgurl
    let nameimg = show nb ++ ext
    putStrLn $ "Downloading "++nameimg

    jpg <- get imgurl
    B.writeFile nameimg jpg
  where
    get url = let uri = case parseURI url of
                          Nothing -> error $ "Invalid URI: " ++ url
                          Just u -> u in
              simpleHTTP (defaultGETRequest_ uri) >>= getResponseBody

main = do
    mapM downloadImg [220..250]

