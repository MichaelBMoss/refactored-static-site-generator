pages = [
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    },
    {git
    "filename": "content/bio.html",
    "output": "docs/bio.html",
    },
    {
    "filename": "content/contact.html",
    "output": "docs/contact.html",
    },
]

for page in pages:
    top_template = open('templates/top.html').read()
    bottom_template = open('templates/bottom.html').read()
    content = open(page['filename']).read()
    combined = top_template + content + bottom_template
    open(page['output'], 'w+').write(combined)
       
    
    
    
    
    
    
    
    
    
    


