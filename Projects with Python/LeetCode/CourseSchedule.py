class Node:
    def __init__ (self, number):
        self.number = number
        self.visited = False
        self.unlock = []
        self.numCoursesNecessary = 0


class Solution:
    def canFinish(self, numCourses, prerequisites):
        # building a graph
        courses = {}
        for p in prerequisites:
            if p[1] not in courses:
                courses[p[1]] = Node(p[1])
            if p[0] not in courses:
                courses[p[0]] = Node(p[0])
            courses[p[0]].numCoursesNecessary += 1
            courses[p[1]].unlock.append(courses[p[0]])

        while (True):
            if numCourses <= 0:
                return True
            NoCourseAvailabe = True
            Visiteds = 0
            for i in courses:
                if courses[i].visited == True:
                    Visiteds += 1
                if courses[i].visited == False and courses[i].numCoursesNecessary == 0:
                    NoCourseAvailabe = False
                    numCourses -= 1
                    courses[i].visited = True
                    for course in courses[i].unlock:
                        course.numCoursesNecessary -= 1

            if Visiteds == len(courses):
                return True
            if NoCourseAvailabe and numCourses > 0:
                return False
            
solution = Solution().canFinish

print(solution(5, [[1,4],[2,4],[3,1],[3,2]]))
