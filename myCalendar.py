class myCalendar:

    name = ""
    date = ""
    professor = ""
    devent = ""

    def devent(self):
        self.set_classes("")
        self.set_date("")
        self.set_event("")
        self.set_professor("")

    def devent(self,class1,professor1,event1,date1):
        self.set_classes(class1)
        self.set_professor(professor1)
        self.set_event(event1)
        self.set_date(date1)
    def set_classes(self, name1):
        self.name = name1
    def  set_date(self,date1):
        self.date = date1
    def set_professor(self,professor1):
        self.professor = professor1
    def set_event(self,event1):
        self.cevent = event1
    def get_class(self):
        return self.name
    def get_professor(self):
        return self.professor
    def get_event(self):
        return self.cevent
    def get_date(self):
        return self.date
    def toString(self):
        return self.get_class()+"\t" +self.get_professor()+"\t"+self.get_event()+"\t"+self.get_date()
    def equals(self,b):
        if self.get_date().strip(" ").replace(" ","").upper() == b.get_date().strip(" ").replace(" ","").upper() and self.get_event().strip(" ").replace(" ","").upper() == b.get_event().strip(" ").replace(" ","").upper() and self.get_professor().strip(" ").replace(" ","").upper() == b.get_professor().strip(" ").replace(" ","").upper() and self.get_class().strip(" ").replace(" ","").upper() == self.get_class().strip(" ").replace(" ","").upper():
            return True
        else:
            return False