import math
class Graph:
    class WeightedEdge:
        def __init__(self, source,dest, weight, times):
            """
            initializes the WeightedEdge class. Adapted from Ed which was posted by Nathan. The complexity of this is
            O(1) since we are only initializing the edge itself.
            :param source: The source of the edge
            :param dest: The destination of the edge
            :param weight: The weight of the edge
            """
            self.dest = dest
            self.weight = weight
            self.ratio = 0
            self.source = source

    def __init__(self, n,starting_liquid):
        """
        initializes the graph class. Adapted from Ed which was posted by Nathan. The complexity of this is
        O(1) since we are only initializing the graph itself.
        :param n:  number of liquids
        :param starting_liquid: the liquid that we are starting with
        """
        self.adj_list = []
        self.num_vertices = n
        self.current_liquid = starting_liquid
        self.trades = 0
        self.best = 0

    def add_directed_edge(self, source, dest, weight):
        """
        Add a directed edge into the adjacency list
        :param source: The source of the edge that we are adding into the graph
        :param dest: The destination of the edge that we are adding into the graph
        :param weight: The weight of the edge
        """
        self.adj_list.append(Graph.WeightedEdge(source,dest, weight,0))

    def clean_slate (self):
        """
        refreshes the memo
        :return: a list of - math.inf multiplied by the amount of vertices.
        """
        return  [-math.inf] * self.num_vertices

def best_trades(prices,starting_liquid,max_trades,townspeople):
    """
    Question 1 in Assignment 4. Utilizes the Bellman Ford Algorithm and allos us to traverse through the graph and use DP
    in order to find the best trades within the constraint that we have (max_trades). The time complexity of this is O(T ∗ M)
    where T is the total number of trades available and M is the maximum trades that we are allowed to have. This is why
    we use Bellman Ford since Bellman Ford also has the same complexity as the question itself.
    :param prices: the list of possible prices
    :param starting_liquid: the liquid that we start with
    :param max_trades: the maximum trades that we are allowed to have
    :param townspeople: the list of townspeople that are available to trade with us.
    :return: returns that maximum amount of money that we can gather within the maximum trades
    """
    graph = Graph(len(prices),starting_liquid)
    # add the trades in one by one as the edge
    for i in range(len(townspeople)):
        for j in range (len(townspeople[i])):
            graph.add_directed_edge(townspeople[i][j][0],townspeople[i][j][1],townspeople[i][j][2])
    #initialize the memo
    weight = graph.clean_slate()
    weight[starting_liquid] = 1
    tradings = []
    first_trade = graph.clean_slate()
    first_trade[starting_liquid] = 1
    #save the memo of all the trades
    tradings.append(first_trade)
    starting_price = prices[starting_liquid]
    #memo to save the largest weight we can have for any given liquid throughout the whole operation
    maximum_weight = graph.clean_slate()
    maximum = 0
    #loops thorugh max_trades time
    for trades in range (1,max_trades+1):
        #whips the memo so that the weight does not accumulate since Bellman Ford relaxes all the edges
        if trades != 1:
            tradings.append(weight)
            weight = graph.clean_slate()
        weight[starting_liquid] = 1
        #checks relaxes the edges one by one, compare with the memo and update it accordingly
        for edge in graph.adj_list:
            current = tradings[trades-1][edge.source] * edge.weight
            #check if it is the current weight is more than the maximum weight and update it accordingly. This is done to
            #make the code more efficient since we could be calculating the price on the fly but it would significantly
            #increase runtime.
            if current != -math.inf and current > tradings[trades-1][edge.dest] and current > weight[edge.dest] and current > maximum_weight[edge.dest]:
                weight[edge.dest] = current
                maximum_weight[edge.dest] = current
    #get the maximum price
    for i in range (len(maximum_weight)):
        current_price = maximum_weight[i] * prices[i]
        if current_price > maximum:
            maximum = current_price

    if maximum < starting_price:
        return starting_price
    return maximum

import math
class Heap():
    """
    Heap class adapted from FIT 1008 Heap class. Edited and added code so that it is now a minHeap that can be used for
    for this assignment.
    """

    def __init__(self):
        """
        Initializes the Heap class. Start with [None] for self.arr.
        The time complexity of this would be O(1)
        """
        self.arr = [None]
        self.length = len(self)

    def __len__(self):
        """
        The time complexity of this would be O(1)
        :return: length of self.arr
        """
        return len(self.arr)

    def smallest_child(self, position) -> int:
        """
        Get the smallest child by comparing both left and right children and see which has the lowest cost.
        :param position: the position of the vertex that we are checking
        The time complexity of this would be O(1)
        :return: position of left or right child depending on which is smaller.
        """
        if 2 * position >= self.length or self.arr[2 * position].cost < self.arr[(2 * position) + 1].cost:
            return position * 2
        else:
            return position * 2 + 1

    def rise(self, position) -> None:
        """
        Allows up to update the self.arr so that we make sure our minHeap is correct. This is done by looping and
        comparing the vertex that we are checking with its parent and see whether it is smaller. Since it is a minHeap,
        smaller elements should be higher that ones that have a lower cost which is why this is important for use to do
        The time complexity is O(N//2) where N is the number of nodes within the heap.
        :param position:
        :return:
        """
        while position// 2 > 0:
            if self.arr[position].cost < self.arr[position // 2].cost:
                self.swap(position, position // 2)
            position = position // 2

    def sink(self, k: int) -> None:
        """
        This allows us to sink the nodes that have a higher cost down to maintain the attribute of minHeap and ensuring
        that the vertex with the largest cost will be further down the heap. The time complexity will be

        :param k:
        :return:
        """
        while 2 * k <= self.length:
            child = self.smallest_child(k)
            if self.arr[k].cost > self.arr[child].cost and k != 0:
                self.swap(child, k)
            k = child

    def serve(self):
        """
        Swaps the bottommost node to the top to pop the root out. Sinks it afterwards to make sure Heap is correct.

        :return:
        """
        self.swap(1, len(self.arr) - 1)
        a = self.arr.pop()
        self.sink(1)
        return a

    def swap(self, position1, position2):
        """
        Swaps the element in the heap. The time complexity is O(1)
        :param position1:
        :param position2:
        """
        self.arr[position1], self.arr[position2] = self.arr[position2], self.arr[position1]

    def find_position(self,vertex):
        """
        Finds the position of the vertex within the heap. Is slightly more time consuming than using a position array however
        due to problems when implementing it, I decided to use this method instead which works well but will increase runtime
        by quite a bit. The time complexity would be O(N) where N is the number of elements in the heap which will always be
        lesser or equal to the total amount of vertexes thus being within the complexity limit.
        :param vertex: The vertex that we are looking for
        :return:
        """
        for i in range(1,len(self.arr)):
            if self.arr[i] == vertex:
                return i

class Vertex():
    def __init__(self, id, cost):
        """
        Initializes the Vertex class. Time complexity is O(1)

        :param id: the vertex id
        :param cost: the cost associated with the vertex
        """
        self.id = id
        self.edges = []
        self.cost = cost
        self.discovered = False
        self.previous = 0

    def clean(self):
        """
        Resets the vertex to make sure we don't have to reinitialize the class again
        """
        self.discovered = False
        self.previous = 0
        self.cost = math.inf

class GraphDijk():
    class WeightedEdge:
        def __init__(self, dest, weight, source):
            """
            Initializes the edge class. Adapted from code uploaded on Ed by Nathan
            :param dest:
            :param weight:
            :param source:
            """
            self.dest = dest
            self.weight = weight
            self.source = source

    def __init__(self, n):
        """
        Initializes the GraphDijk class, create a list of vertex into our adjacency list.
        The time complexity is O(n) where n is the number of vertices

        :param n:
        """
        self.adj_list = [Vertex(x, math.inf) for x in range(n)]
        self.num_vertices = n

    def add_directed_edge(self, source, dest, weight):
        """
        Adds an edge into our adjacency list

        :param source:
        :param dest:
        :param weight:
        :return:
        """
        self.adj_list[source].edges.append(GraphDijk.WeightedEdge(dest, weight, source))

    def dijkstra(self, start, end):
        """
        Dijkstra algorithm to find the path. Time complexity is  O ( V + E l o g V ) . where V is the number of vertices
        and E is the number of edges. This allows us to serve the minimum element from the minHeap every iteration, and
        relax all of its edges and update its position in the Heap. The path will then be regenerated through backtracking
        the Vertex's previous node.

        :param start: Start of the graph
        :param end: End of the graph
        :return: Cost and Path with the Lowest Cost
        """
        source = self.adj_list[start]
        source.cost = 0
        minHeap = Heap()
        minHeap.arr.append(source)
        while len(minHeap.arr) > 1:
            u = minHeap.serve()
            u.visited = True
            #loops through every edge and relax it one by one
            for edge in u.edges:
                v = edge.dest
                a = minHeap.find_position(self.adj_list[v])
                #checks whether it already exists in the heap
                if self.adj_list[v].discovered == False:
                    self.adj_list[v].discovered = True
                    self.adj_list[v].cost = u.cost + edge.weight
                    self.adj_list[v].previous = u
                    minHeap.arr.append(self.adj_list[v])
                    minHeap.rise(len(minHeap.arr)-1)
                else:
                    if self.adj_list[v].cost > u.cost + edge.weight:
                    #checks if the cost is smaller than the one already within our heap.
                        self.adj_list[v].cost = u.cost + edge.weight
                        self.adj_list[v].previous = u
                    if a is not None:
                        minHeap.rise(minHeap.find_position(self.adj_list[v]))

        #reconstructs the path through backtracking and reseting the vertex to default value so that we can reuse it in
        #the next iterations.
        path = []
        found = False
        ending = self.adj_list[end-1]
        path.append(end-1)
        cost = ending.cost
        prev = end -1
        while found == False:
            current = self.adj_list[prev].previous
            if current.id != start:
                path.append(current.id)
                prev = current.id
            else:
                path.append(current.id)
                found = True
        for i in range (len(self.adj_list)):
            self.adj_list[i].clean()
        return ([cost, path])


def opt_delivery(n, roads, start, end, delivery):
    """
    Calls the dijkstra algorithm above four times. Once for the start to end, and the rest will be used to reconstruct
    the path from start to start of delivery, start of delivery to destination of delivery, and finally from the
    destination of delivery to end. This allows us to combine the three and compare it to the first run of dijkstra
    (start - end) to compare whether it is more worth it to pickup and deliver or we should just travel to the end
    straight away instead
    The time complexity is  O ( V + E l o g V ) . where V is the number of vertices and E is the number of edges. It
    will be multiplied by four since we are calling the dijkstra four times but since it is a constant, we are able to
    omit it from our time complexity.

    :param n: number of cities
    :param roads: all roads available
    :param start: city that we start at
    :param end: city that we need to end at
    :param delivery: the path we take if we were to choose to deliver
    :return:
    """
    graph = GraphDijk(n)
    #adds the edges into the graph
    for road in roads:
        graph.add_directed_edge(road[0], road[1], road[2])
        graph.add_directed_edge(road[1], road[0], road[2])
    start_end = graph.dijkstra(start, end + 1)
    start_pickup =graph.dijkstra(start, delivery[0] + 1)
    pickup_delivery = graph.dijkstra(delivery[1], end + 1)
    delivery_end = graph.dijkstra(delivery[0], delivery[1] + 1)
    #calculate the total cost that we get if we choose to pickup
    pickup = start_pickup[0] + pickup_delivery[0] + delivery_end[0] + -delivery[2]
    if start_end[0] < pickup or start_end[0] == pickup:
        final_path = []
        for i in range(len(start_end[1]) - 1, -1, -1):
            final_path.append(start_end[1][i])
        return start_end[0],final_path
    else:
        # recontruct and combine the paths and then add up the cost
        final_path = []
        cost = 0
        for i in range (len(start_pickup[1])-1,-1,-1):
            final_path.append(start_pickup[1][i])
        cost += start_pickup[0]
        for i in range(len(delivery_end[1]) - 2, 0, -1):
            final_path.append(delivery_end[1][i])
        for i in range(len(pickup_delivery[1]) - 1, -1, -1):
            final_path.append(pickup_delivery[1][i])
        cost += pickup_delivery[0]
        cost += delivery_end[0]
        cost -= delivery[2]
        return cost,final_path



