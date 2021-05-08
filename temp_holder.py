
response_text = get_reponse_text(listing_url)
# implementation
if response_text != False:
    bsoup = create_bsoup(response_text)
    articles = bsoup.select(
        ".obj_article_summary"
    )
    usable_volume = get_volume(bsoup)
    # create blank document with volume name+ issue
    mydoc = docx.Document()
    # define working document name. Prefix volume+issue details with journal name
    file_name = f"{usable_volume}.docx"
    # create style
    style = mydoc.styles['Normal']
    font = style.font
    font.name = "Times New Roman"
    font.size = Pt(11)
    mydoc.save(file_name)

    i = 0
    for a in articles:
        usable_title = get_title(a)
        usable_authors = get_authors(a)
        usable_page_number = get_page_number(a)
        usable_article_url = get_article_url(a)
        usable_abstract = fetch_abstract(usable_article_url)

        mydoc = docx.Document(file_name)
        paragraph = mydoc.add_paragraph(
            f"{usable_authors}.")
        paragraph.add_run(f"{usable_title}.").bold = True
        paragraph.add_run(
            f"{usable_volume}: {usable_page_number}.  {usable_abstract}")
        paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        mydoc.add_paragraph("")
        mydoc.save(file_name)
        i += 1
        print(f"Processed: {i}")
    print("All complete!!!")
