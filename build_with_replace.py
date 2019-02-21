template = open("templates/base.html").read()
index_content = open("content/index.html").read()
finished_index_page = template.replace("{{content}}", index_content)
open("docs/index.html", "w+").write(finished_index_page)

template = open("templates/base.html").read()
index_content = open("content/contact.html").read()
finished_index_page = template.replace("{{content}}", index_content)
open("docs/contact.html", "w+").write(finished_index_page)

template = open("templates/base.html").read()
index_content = open("content/bio.html").read()
finished_index_page = template.replace("{{content}}", index_content)
open("docs/bio.html", "w+").write(finished_index_page)
