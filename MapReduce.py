import json


l=[]
class MapReduce:
    
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        #print(self.result)
        return self.result.append(value) 
    

    def execute(self, data, mapper, reducer):

        for line in data:
            record = json.loads(line)
            #print(record)
            mapper(record)
        
        for key in self.intermediate:
            reducer(key, self.intermediate[key])
            #print("hola" + str(self.result))
        l=self.result
        f=open("kk.txt","w")
        for i in l:
            f.write(str(i)+ "\n")
            #print(i)
        f.close()
        # l=f=open("kk.txt","w")
        # f.write(str(self.result))
        # f.close()
        #jenc = json.JSONEncoder(encoding='latin-1')
        jenc = json.JSONEncoder()


    