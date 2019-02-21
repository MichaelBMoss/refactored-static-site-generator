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

def combine_pages(list_number):       
        template = open("templates/base.html").read()
        content = open(pages[list_number]['filename']).read()
        combined = template.replace("{{content_placeholder}}", content)
        return combined

def create_page(list_number):      
        page_data = combine_pages(list_number)  
        open(pages[list_number]['output'], "w+").write(page_data) 

def main():
    for num in range (0, 3):
        create_page(num)

main()


