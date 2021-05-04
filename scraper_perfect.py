from bs4 import BeautifulSoup
import requests
import docx
"""
    set listing url address and output word document file name
    in the listing_url and doc_path variables

"""
listing_url = "https://www.ajol.info/index.php/ahs/issue/view/10828"
doc_path = 'hybreed_spider.docx'


def get_volume(bsoup):
    try:
        get_volume = bsoup.select(
            "#pkp_content_main > div.page.page_issue > nav > ol > li.current")
        volume = get_volume[0].getText().strip()
        return volume
    except IndexError:
        volume = ". No volume Number Not Found! "
        return volume


def get_page_number(a):
    try:
        page_number = a.select(
            '.obj_article_summary .pages')[0].getText().strip().replace("\t", "")
        return page_number

    except IndexError:
        page_number = ". Page Number Not Found! "
        return page_number


def get_title(a):
    try:
        title = a.select('.obj_article_summary .title>a')[
            0].getText().strip().replace("\t", "")
        return title
    except IndexError:
        title = ". Title Not Found! "
        return title


def get_article_url(a):
    try:
        article_url = a.select('.obj_article_summary .title>a')[0].get('href')
        return article_url
    except IndexError:
        article_url = ". Article link Not Found! "
        return article_url


def get_authors(a):
    try:
        authors = a.select('.meta .authors')[
            0].getText().strip().replace("\t", "")
        return authors
    except IndexError:
        authors = ". Authors Not Found! "
        return authors


def fetch_abstract(url):
    r_text = get_reponse_text(url)
    if r_text != False:
        abstract_bsoup = create_bsoup(r_text)
        try:
            abstract = abstract_bsoup.select(
                "#pkp_content_main > div.page.page_article > article > div > div.main_entry > div.item.abstract > p:nth-child(2)")
            abstract = abstract[0].getText()
        except IndexError:
            try:
                abstract = abstract_bsoup.select(
                    "#pkp_content_main > div.page.page_article > article > div > div.main_entry > div.item.abstract")
                abstract = abstract[0].getText()
            except IndexError:
                abstract = ". No Abstract Found! "

        return abstract


def get_reponse_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        response_text = response.text
        return response_text
    else:
        return False


def create_bsoup(response_text):
    bsoup = BeautifulSoup(response_text, 'html.parser')
    return bsoup


response_text = get_reponse_text(listing_url)
# implementation
if response_text != False:
    bsoup = create_bsoup(response_text)
    articles = bsoup.select(
        ".obj_article_summary"
    )
    usable_volume = get_volume(bsoup)
    i = 0
    for a in articles:
        usable_title = get_title(a)
        usable_authors = get_authors(a)
        usable_page_number = get_page_number(a)
        usable_article_url = get_article_url(a)
        usable_abstract = fetch_abstract(usable_article_url)

        mydoc = docx.Document(doc_path)
        mydoc.add_paragraph(
            f"{usable_authors}. {usable_title}. {usable_volume}: {usable_page_number}.  {usable_abstract}")
        mydoc.save(doc_path)
        i += 1
        print(f"Processed: {i}")
    print("All complete!!!")
