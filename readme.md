# Page title crawler

## Installation
Install Python 2.7
https://www.python.org/downloads/release/python-2713/

pip install scrapy
pip install pandas

git clone <project git repo>

## Usage
scrapy crawl htmltitle -a file_path=OTV_Video_Stream_201609.csv -a domain_index=1 -a url_index=7 -o title.txt

### Arguments
-a file_path - the file contains the domains and URLs need to be crawled.
-a domain_index - the column index contains domain, starts from 0.
-a url_index - the column index contains url, starts from 0.
-o - output file.
