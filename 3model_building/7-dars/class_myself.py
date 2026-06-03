class StudentInfo:
    def __init__(self, name, university, major, languages):
        self.name       = "Otakhanov Asqarali"
        self.university = " Inje University"
        self.major      = "International Trade"
        self.languages   = ["Uzbek", "Korean", "English"]

    def introduce(self):
        return f"Assalomu aleykum! Men {self.name}, {self.university} da o'qiydigan talabaman."

    def get_info(self):
        return {
            "Ismi":             self.name,
            "Universiteti":     self.university,
            "Mutaxassisligi":   self.major,
            "Tillari":          self.languages
        }

student = StudentInfo()

print(student.introduce())
print(student.get_info())