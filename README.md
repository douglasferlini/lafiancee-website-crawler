# lafiancee-website-crawler
Web crawler for lafiancee.com.br website.  
  
## Instructions
1.Execute "docker build -t lafiancee-crawler ." inside the root folder of this project to generate the docker container.  
2.Execute "docker run --name lafiancee-crawler --rm -p 8000:8000 --network=host lafiancee-crawler" to start the container.
3.Access http://localhost:8000/ to download the json result.
