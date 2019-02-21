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

for page in pages:
    title = page['title']
    link = page['link']
    template = open("templates/base.html").read()
    content = open(page['filename']).read()
    combined1 = template.replace("{{content_placeholder}}", content)
    open('docs/temp.html', "w+").write(combined1) 
    combined2 = open("docs/temp.html").read()
    combined3 = combined2.replace("{{title_ph}}", title)
    open('docs/temp.html', "w+").write(combined3)
    combined4 = open("docs/temp.html").read()
    combined5 = combined4.replace(link, "box")
    open(page['output'], "w+").write(combined5) 
    
