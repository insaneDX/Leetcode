class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Initialize reachability matrix for Courses
        reachability_matrix = [[False for j in range(numCourses)] for i in range(numCourses)]

        # Mark direct prerequisites in the reachability matrix
        for (a,b) in prerequisites:
            reachability_matrix[a][b] = True

        # Apply the Floyd-Warshall to trace path of intermediate prerequisites courses
        for k in range(numCourses): # intermediate Node
            for i in range(numCourses): # Start Node
                for j in range(numCourses): # End Node
                    # If course i is a prerequisite of course k and course k is a prerequisite of course j                    
                    if (reachability_matrix[i][k] and reachability_matrix[k][j]):
                        reachability_matrix[i][j] = True
    
        # return prerequisite matrix for the asked queries
        return [reachability_matrix[u][v] for u,v in queries]

# Time Complexity
# creating a numCourses x numCourses matrix, which takes O(numCourses^2) time.
# Marking direct Prerequisites -> Time : O(P), where P is the len of prerequisites.
# The Floyd-Warshall algorithm involves three nested loops, each iterating numCourses times. This results in a time complexity of O(numCourses^3).
# Processing Queries: This step involves iterating through the queries list, which takes O(Q) time, where Q is the number of queries.