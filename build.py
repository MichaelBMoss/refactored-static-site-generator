def main():
# concatenates top 3 pages to create my home page
    top_template = open('templates/top.html').read()
    bottom_template = open('templates/bottom.html').read()
    content = open('content/home.html').read()
    mike_moss_home = top_template + content + bottom_template
    open('docs/mike_moss_home.html', 'w+').write(mike_moss_home)

# concatenates top 3 pages to create my bio page
    top_template = open('templates/top.html').read()
    bottom_template = open('templates/bottom.html').read()
    content = open('content/bio.html').read()
    mike_moss_bio = top_template + content + bottom_template
    open('docs/mike_moss_bio.html', 'w+').write(mike_moss_bio)

# concatenates top 3 pages to create my contact page
    top_template = open('templates/top.html').read()
    bottom_template = open('templates/bottom.html').read()
    content = open('content/contact.html').read()
    mike_moss_contact = top_template + content + bottom_template
    open('docs/mike_moss_contact.html', 'w+').write(mike_moss_contact)

#runs the main function    
if __name__ == "__main__":
    main()
