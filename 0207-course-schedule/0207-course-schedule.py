class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Create a graph with each course as a key and an empty list as its value
        graph = {i:[] for i in range(numCourses)}

        # Populate the graph with the prerequisites
        for course, preq in prerequisites:
            graph[course].append(preq)
        
        # Set to keep track of visited courses
        visited = set()
        # Set to keep track of the current path in the DFS
        current_path = set()

        def dfs(course):
            # If the course is already in the current path, a cycle is detected
            if course in current_path:
                return False
            # If the course has already been visited, no need to visit again
            if course in visited: 
                return True

            # Add the course to the current path
            current_path.add(course)

            # Recursively visit all the prerequisites
            for preq in graph[course]:
                if not dfs(preq):
                    return False
            
            # Remove the course from the current path and mark it as visited
            current_path.remove(course) 
            visited.add(course)
        
            return True

        # Check each course to see if it can be completed
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
