pages = [
{
"filename": "content/home.html",
"output": "docs/mike_moss_home.html",
},
{
"filename": "content/bio.html",
"output": "docs/mike_moss_bio.html",
},
{
"filename": "content/contact.html",
"output": "docs/mike_moss_contact.html",
},

]



for page in pages:
    top_template = open('templates/top.html').read()
    bottom_template = open('templates/bottom.html').read()
    content = open(page['filename']).read()
    combined = top_template + content + bottom_template
    open(page['output'], 'w+').write(combined)
       
    
    
    
    
    
    
    
    
    
    


