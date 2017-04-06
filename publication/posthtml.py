#!/usr/bin/env python3

from os.path import join as jpath
import subprocess

bibtexfile	= "hazirbas.bib"
basehtml	= "hazirbas.html"
baseurl		= "https://hazirbas.github.io/"
baseurl		= ""
imurl		= jpath(baseurl, "")
bibtex2html	= "bibtex2html -s ieeetr -d -r -nf url source -noheader -nofooter -nodoc -linebreak -nf doi doi -nodoi -noabstract "

subprocess.check_output(bibtex2html + ' ' + bibtexfile, shell=True)

def centertr(html):
	for inx, line in enumerate(html):
		if "<tr valign=" in line:
			html[inx] = line.replace("top", "middle")
	return html
	
def itemnum2imlink(html):
	for inx, line in enumerate(html):
		if "[<a name=" in line:
			line = line[0:line.find("</a>]")-1] + '\n'
			line = line.replace("[<a", "<img")
			line = line.replace("name=\"", "src=\"" + imurl)
			line = line. replace("\">", ".png\" style=\"width:350px; height:100px; vertical-align:middle;\">")
			html[inx] = line
	return html

with open(basehtml, 'r') as infile:
	html	= infile.readlines()
	html	= [line if line != "<p>\n" else "" for line in html]
	html[1] = "<table class=\"borderless\">\n"
	# html	= centertr(html)
	html	= itemnum2imlink(html)

with open(basehtml, 'w') as outfile:
	outfile.writelines(html)


# class htmlParser(HTMLParser):