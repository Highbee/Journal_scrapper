"""
    ------------------------dev notes---------------------
    Needs to treat "?."



    ----------------
    Author: Ibrahim, Ibrahim Opeyemi
        Email: IbrahimIbrahimOpeyemi@gmail.com
        Phone: 08107321115
    Version: Not set yet
    This script copies articles from Ajol. It works with ajol and
         probably any aggregator sites using exactly the same HTML template
    ---------------usage-------------
    1.  set listing URL address and output word document file name
    in the listing_url and doc_path variables
    ---------------dependencies-----------
    1.  BeautifulSoup4==4.9.1
    2.  requests==2.24.0


"""
from bs4 import BeautifulSoup
import requests
import docx
