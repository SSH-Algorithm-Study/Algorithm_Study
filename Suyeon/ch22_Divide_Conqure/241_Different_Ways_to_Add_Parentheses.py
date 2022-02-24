class Solution:
    expression = ""
    size = 0
    answer = []

    def calculate(self, a, opt, b):
        print(a,opt,b)
        if self.expression[opt] == "+":
            return a+b
        elif self.expression[opt] == "-":
            return a-b
        else:
            return a*b

    def partiton(self, head,tail):
        global expression

        if head == tail:
            return int(self.expression[head])
        p = head
        return self.calculate(self.partiton(head, p),p+1, self.partiton(p+2,tail))

    def merge(self,head,tail):
        p = head
        while p < self.size-2:
            print(p)
            self.answer.append(self.calculate(self.partiton(head,p), p+1, self.partiton(p+2,tail)))
            p += 2


    def diffWaysToCompute(self, expression: str):
        self.expression = expression
        self.size = len(expression)
        self.merge(0,self.size-1)

        return self.answer



class Solution:
    def calculate(self,left,right,opt):
        result = []
        for l in left:
            for r in right:
                result.append(eval(str(l) + opt + str(r)))
        return result

    def diffWaysToCompute(self, expression: str):
        answer = []
        if expression.isdigit():
            return [expression]

        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])

                answer.extend(self.calculate(left,right,expression[i]))

        return answer

