def topologicalSort(jobs, dependencies):
    jobGraph = createJobGraph(jobs, dependencies)
    return getOrderedJobs(jobGraph)

def createJobGraph(jobs, dependencies):
    graph = JobGraph(jobs)
    for job, dependency in dependencies:
        graph.addDependency(job, dependency)
    return graph

def getOrderedJobs(graph):
    orderedJobs = []
    nodesWithNoPrerequisites = list(filter(lambda node: node.numOfPrerequisites == 0, graph.nodes))
    while len(nodesWithNoPrerequisites):
        node = nodesWithNoPrerequisites.pop()
        orderedJobs.append(node.job)
        removeDependencies(node, nodesWithNoPrerequisites)
    graphHasEdges = any(node.numOfPrerequisites for node in graph.nodes)
    return [] if graphHasEdges else orderedJobs

def removeDependencies(node, nodesWithNoPrerequisites):
    while len(node.dependencies):
        dependency = node.dependencies.pop()
        dependency.numOfPrerequisites -= 1
        if dependency.numOfPrerequisites == 0:
            nodesWithNoPrerequisites.append(dependency)

class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)
    
    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def addDependency(self, job, dependency):
        jobNode = self.getNode(job)
        dependencyNode = self.getNode(dependency)
        jobNode.dependencies.append(dependencyNode)
        dependencyNode.numOfPrerequisites += 1

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

class JobNode:
    def __init__(self, job):
        self.job = job
        self.dependencies = []
        self.numOfPrerequisites = 0