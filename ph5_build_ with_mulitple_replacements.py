pages = [
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "Mike Moss Home",
    "link": "home_ph",
    },
    {
    "filename": "content/bio.html",
    "output": "docs/bio.html",
    "title": "Mike Moss Bio",
    "link": "bio_ph",
    },
    {
    "filename": "content/contact.html",
    "output": "docs/contact.html",
    "title": "Mike Moss Contact",
    "link": "contact_ph",
    },
]


def main():
    for page in pages:
        template = open("templates/base.html").read()
        content = open(page['filename']).read()
        combined1 = template.replace("{{content_placeholder}}", content)
        combined2 = combined1.replace("{{title_ph}}", page['title'])
        combined3 = combined2.replace(page['link'], "box")
        open(page['output'], "w+").write(combined3)
      
main()
