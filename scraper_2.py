import requests
from bs4 import BeautifulSoup
import docx


def get_authors():
    try:
        authors_container = bsoup.select(
            "#pkp_content_main > div.page.page_article > article > div > div.main_entry > ul")
        # print(type(authors))
        authors_list = ''.join([a.getText().strip().replace("\t", "").replace("\n", ';')
                                for a in authors_container])
        return authors_list

    except IndexError:
        authors_list = "No authors;"
        return authors_list


# get volume info
def get_volume():
    try:
        get_volume = bsoup.select(
            "#pkp_content_main > div.page.page_article > nav > ol > li:nth-child(3) > a")
        volume = get_volume[0].getText().strip()
        return volume
    except IndexError:
        volume = "No volume Specified"
        return volume
    # get abstract


def get_abstract():

    try:
        abstract = bsoup.select(
            "#pkp_content_main > div.page.page_article > article > div > div.main_entry > div.item.abstract > p:nth-child(2)")
        abstract = abstract[0].getText()
    except IndexError:
        try:
            abstract = bsoup.select(
                "#pkp_content_main > div.page.page_article > article > div > div.main_entry > div.item.abstract")
            abstract = abstract[0].getText()
        except IndexError:
            abstract = "No abstract"

    return abstract


def get_title():

    try:
        title = bsoup.select(
            "#pkp_content_main > div.page.page_article > article > h1")
        title = title[0].getText()
        return title
    except IndexError:
        title = "No Title"
        return False


def get_page_number(article_title, listing_url, i):
    try:
        listing_response = requests.get(listing_url)
        if listing_response.status_code == 200:
            listing_html = listing_response.text

            listing_bsoup = BeautifulSoup(listing_html, 'html.parser')
        pages_list = listing_bsoup.select(".obj_article_summary .pages")

        page = pages_list[i].getText()
        return page

    except IndexError:
        page = "No page Found"
        return page


min_article_url_no = 206001
max_article_url_no = 206090
i = 0
while min_article_url_no <= max_article_url_no:
    response = requests.get(
        'https://www.ajol.info/index.php/ahs/article/view/'+str(min_article_url_no))

    if response.status_code == 200:
        html_content = response.text
        bsoup = BeautifulSoup(html_content, 'html.parser')

        authors_list = get_authors()
        volume = get_volume()
        abstract = get_abstract()
        title = get_title()
        if title == False:
            min_article_url_no += 1
            continue
        # get get

        pn = get_page_number(
            title, "https://www.ajol.info/index.php/ahs/issue/view/19602", i)

        doc_path = 'hybreed_spider.docx'
        mydoc = docx.Document(doc_path)
        mydoc.add_paragraph(
            f" {authors_list}. {title}.{pn} {volume}. {abstract}")
        mydoc.save(doc_path)
        i += 1
    min_article_url_no += 1

    print(f"(last article url_no: {min_article_url_no}), (last i: {i})")

# file = open("spider.txt", 'w', encoding='utf-8')
# file.write(f"\n \n {volume}{authors_list}{abstract}")
# file.close()

# print(f"\n \n {volume}{authors_list}{abstract}")
