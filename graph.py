def yaal(adj, v, w):
	adj[v].append(w)
	adj[w].append(v)
	return adj

def rangamizi(adj, V):
	
	# Which color we've used for nth vertex
	result = [-1] * V
	result[0] = 0;

	# Has it been used.
	available = [False] * V

	for u in range(1, V):
		print(f'Adjecant of {u}: {adj[u]}')

		# Finding already colored.
		for i in adj[u]:
			if (result[i] != -1):
				print(f'changed {result[i]} to true.')
				available[result[i]] = True

		# Finding which color is available.
		cr = 0
		print(f'Available is: {available}\n')
		while cr < V:
			if (available[cr] == False):
				break
			cr += 1
		

		# Coloring.
		result[u] = cr

		# Resetting.
		print(f'New result is: {result}\n')
		for i in adj[u]:
			if (result[i] != -1):
				available[result[i]] = False

	for u in range(V):
		print(f"Vertex {u} used Color {result[u]}")

if __name__ == '__main__':
	
	g1 = [[] for i in range(5)]
	g1 = yaal(g1, 0, 1)
	g1 = yaal(g1, 0, 2)
	g1 = yaal(g1, 1, 2)
	g1 = yaal(g1, 1, 3)
	g1 = yaal(g1, 2, 3)
	g1 = yaal(g1, 3, 4)
	rangamizi(g1, 5)
	print('------------------------------------------------\n')

	g2 = [[] for i in range(5)]
	g2 = yaal(g2, 0, 1)
	g2 = yaal(g2, 0, 2)
	g2 = yaal(g2, 1, 2)
	g2 = yaal(g2, 1, 4)
	g2 = yaal(g2, 2, 4)
	g2 = yaal(g2, 4, 3)
	rangamizi(g2, 5)
