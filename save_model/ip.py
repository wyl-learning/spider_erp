ip = ["10.0.128.1","10.0.128.1","10.0.127.1","10.0.128.2"]
company = {
    "1":"company",
    "2":"company"
}
# company1 "10.0.127.0"-"10.0.127.125"
# company2 "10.0.127.126"-"10.0.127.255"
class ip():
    def __init__(self,wei1,wei2,wei3,wei4):
        self.wei1 = wei1
        self.wei2 = wei2
        self.wei3 = wei3
        self.wei4 = wei4
        self.ip = str(wei1)+"."+str(wei2)+"."+str(wei3)+"."+str(wei4)
list1 = [1]*10
print(list1)
