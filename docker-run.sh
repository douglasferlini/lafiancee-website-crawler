#defines the http port for the http server exposing the output file 
HTTP_PORT=${1:-8000}
#starts the container 
docker run --name lafiancee-crawler --rm -d -p ${HTTP_PORT}:8000 -v $(pwd)/out:/var/dresses/ lafiancee-crawler
