pages = [
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    },
    {
    "filename": "content/bio.html",
    "output": "docs/bio.html",
    },
    {
    "filename": "content/contact.html",
    "output": "docs/contact.html",
    },
]

for page in pages: 
    template = open("templates/base.html").read()
    content = open(page['filename']).read()
    combined = template.replace("{{content_placeholder}}", content)
    open(page['output'], "w+").write(combined) 
    

