class product:
    def __init__(self,productID,productName,previousProduct,nextProduct,askPrice,askQty,bidPrice,bidQty):
        self.productID = productID
        self.productName=productName
        self.previousProduct=previousProduct
        self.nextProduct=nextProduct
		self.Asks={}

class outright(product):

class spread(product):
    def __init__(self,productID,productName,previousProduct,nextProduct,outrightA,outrightB):
        product.__init__(self,productID,productName,previousProduct,nextProduct,spreadlength)
        self.outrightA=outrightA
        self.outrightB=outrightB
        self.spreadLength=spreadLength

class fly(product):
    def __init__(self,productID,productName,previousProduct,nextProduct,spreadA,spreadB):
        product.__init__(self,productID,productName,previousProduct,nextProduct)
        self.spreadA=spreadA
        self.spreadB=spreadB
            
        
