class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        solutions = set()

        def genPar(builder, openers, closers):
            if len(builder) == n * 2:
                solutions.add(builder)
                return
            
            if openers < n:
                genPar(builder + '(', openers + 1, closers)

            if closers < openers:
                genPar(builder + ')', openers, closers + 1)


        
        genPar('', 0, 0)
        return solutions


