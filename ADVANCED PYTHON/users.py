class Users:
    data=[

        {"id":1,"username":"anu","email":"anu@gmail.com","password":"password@123"},
        {"id":2,"username":"achu","email":"achu@gmail.com","password":"password@123"},
        {"id":3,"username":"ammu","email":"ammu@gmail.com","password":"password@123"},
        {"id":4,"username":"manu","email":"manu@gmail.com","password":"password@123"},
        {"id":5,"username":"Thanu","email":"thanu@gmail.com","password":"password@123"},
        {"id":6,"username":"ann","email":"ann@gmail.com","password":"password@123"},
       
        ]
    # get all data
    def get_all_data(self):
        #print(self.data)
        return self.data
    # get one data of a user
    def get_one_data(self,id):
        for u in self.data:
            if u.get("id")==id:
                print(u)
    # def get_one_data(self,index):
    #     print(self.data[index])
    # add a user to data
    def add_user(self,item):
        for u in self.data:
            if u.get("id")==item.get("id"):
                print("id already exist")
                break
                
        else:
            self.data.append(item)
            #print(self.data)
    # delete a user
    def delete_user(self,id):
        for u in self.data:
            if u.get("id")==id:
                self.data.remove(u) 

   # update

    def update(self,id,value):
        for user in self.data:
            if user.get("id")==id:
                pos=self.data.index(user)
                self.data[pos]=value

    

obj=Users()
#obj.get_all_data()
#print(obj.get_all_data()) #if return is inside a function/method then we have to print while calling the function/method
#obj.get_one_data(4)
#obj.add_user({"id":7,"username":"arun","email":"aru@gmail.com","password":"password@123"})
# obj.delete_user(5)
obj.update(5,{"id":5,"username":"arun","email":"aru@gmail.com","password":"password@123"})
print(obj.get_all_data())