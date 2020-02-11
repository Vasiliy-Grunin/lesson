class Student(object):
    def __init__(self, name, **kwargs):
        self.name = name
        self.exam = 0
        self.labs = []
        self.conf={}
        self.conf.update(kwargs)


    def make_lab(self, m, n=1):
        if m > self.conf[0]:
            m = 30
        if n > len(self.labs):
            self.labs.append(m)
        self.labs[n] = m

    def make_exam(self, m=0.0):
        if m > self.conf[0]:
            m = self.conf[0]
        self.exam = m
        return id(self.exam)

    def is_certified(self):
        tuple = sum(self.labs) + self.exam
        you = False
        if float(tuple / 100) >= self.conf.get("k"):
            you = True
        elif float(tuple / 100) <= self.conf.get("k"):
            you = False
        return sum, you


def main():
    #name = input("write your name: ")
    #arr = map(dict, input())
    arr= Student({
        'exam_max': 30,
        'lab_max': 45,
        'lab_num': 5,
        'k': 0.6
    })
    name="vas"
    student = Student(name,exam_max =30, lab_max= 45, lab_num =5, k = 0.6)
    print(student.is_certified())


main()
