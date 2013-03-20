links = {'A':['B','C'],'B':['C'],'C':[]} ## replace with an adjacency matrix . i.e. link[A] = the pages that A links to 
_l = {}
d = 0.85
linked_to = {} ## linked_to[A] = the list of pages that link to A

def fill_data():
	for page in links.keys():
		_l[page] = len(links[page])

	for page in links.keys():
		for link in links[page]:
			linked_to.setdefault(link,[]).append(page) #may not change the global object, may just change this instance

def generate_pagerank(links):
	"""Takes a dictionary, links, and returns a dictionary, pageRank
	for all urls in links"""
	total_pages = links.keys()
	# for i in total_pages:
	# 	page_directory # keep a page directory separate from the pageranks
	pageRankings = {}
	for url in links.keys():
		pageRankings.setdefault(url, 1/len(links.keys())) # returns stuff - what do we do with this return?
	counter = 0
	while True:
		new_page_ranks = {}
		for page in pageRankings.keys():
			new_page_ranks[page] = new_pagerank(page,pageRankings)
		print "On iteration {} The new page ranks are: {}".format(counter,new_page_ranks)
		if new_page_ranks == pageRankings:
			break
		else:
			pageRankings = new_page_ranks
			counter +=1

def new_pagerank(page,current_PageRankings):
	running_sum = 0
	if page not in linked_to.keys():
		return 0
	for page in linked_to[page]:
		contribution = current_PageRankings[page]/_l[page]
		running_sum += contribution # the amount that each page contributes to the currrent page's PR
	return (1-d) + d*running_sum

if __name__ == '__main__':
	fill_data()
	generate_pagerank(links)



#d = 0.85
#PR(A)= (1-d) + d*sum(PG(X=>A)/((X=>.count)))