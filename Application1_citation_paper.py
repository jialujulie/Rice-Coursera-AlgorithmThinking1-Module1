import alg_load_graph
import Project1_graphs
import matplotlib.pyplot as plt

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


citation_graph = alg_load_graph.load_graph(CITATION_URL)

#citation_graph = Project1_graphs.EX_GRAPH2

indegree_distribution =  Project1_graphs.in_degree_distribution(citation_graph)

print len(indegree_distribution)

sum = sum(indegree_distribution.values())

normalize_dist = [indegree_distribution[key]/float(sum) for key in indegree_distribution.keys()]

#print indegree_distribution.keys()
#print normalize_dist
plt.loglog(indegree_distribution.keys(),normalize_dist, linestyle= 'None', marker =u'o')
plt.title('loglog plot - citation distribution')
plt.xlabel('Number of citations')
plt.ylabel('Fraction for each cited paper')
#plt.scatter(indegree_distribution.keys(),normalize_dist)

plt.show()

