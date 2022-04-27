
from mysqlconnetion import connectToMySQL
# model the class after the friend table from our database
class  User:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.communite = data['communite']
        
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        #this get_all is a method it will get all your file 
        query = "SELECT * FROM users;"
        # and this will select which on you and how many
        result = connectToMySQL('awet_schema').query_db(query)
        #and this will connect it and send you the files you need
        users = []
        # now the users is emty in the web page
        for u in result:
            # this will four loop the data and will add the file to the page 
            users.append( cls(u) )
        # and this will return you a list of dicantionarys
        return users
    @classmethod
        #this will save the data on the web page and it will display them and also in the database
    def save( cls,data):
        query = "INSERT INTO users (name,email,communite) VALUES (%(name)s,%(email)s,%(communite)s);"
        # comes back as a new row of id
        result = connectToMySQL('awet_schema').query_db(query, data)
        #and this will return the file or the dichnery or instaintec
        return result