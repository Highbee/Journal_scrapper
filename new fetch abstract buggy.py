def fetch_abstract(url):
    r_text = get_reponse_text(url)
    if r_text != False:
        abstract_bsoup = create_bsoup(r_text)
        try:
            abstract = abstract_bsoup.select(
                "#pkp_content_main > div.page.page_article > article > div > div.main_entry > div.item.abstract > p")
            abstract_text = "".join([a.getText() for a in abstract])
        except IndexError:
            try:
                abstract = abstract_bsoup.select(
                    "#pkp_content_main > div.page.page_article > article > div > div.main_entry > div.item.abstract")
                abstract_text = abstract[0].getText()
            except IndexError:
                abstract_text = ". No Abstract Found! "

        return abstract_text
