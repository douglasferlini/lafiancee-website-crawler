#!/bin/bash
#variable for the output file
OUTPUT_PATH=${OUTPUT_PATH:-"/var/dresses/data.json"}
#enters in dresses directory
cd dress
#executes the scraping
scrapy crawl dress -o ${OUTPUT_PATH}
#gets the output dir path
OUTPUT_DIR=`dirname ${OUTPUT_PATH}`
#enter in the output dir
cd ${OUTPUT_DIR}
#exposes the file in a simple http server
python -m http.server

