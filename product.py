class product:
    def __init__(self,productID,productName,previousProduct,nextProduct,askPrice,askQty,bidPrice,bidQty):
        self.productID = productID
        self.productName=productName
        self.previousProduct=previousProduct
        self.nextProduct=nextProduct
		self.prices={askPrice:[askQty,'ASK'],bidPrice:[bidQty,'BID']}
	def priceUpdate(self,price,qty,type):
		self.prices.update({price:[qty,type]})
		

class strategy(product):
    def __init__(self,productID,productName,previousProduct,nextProduct,askPrice,askQty,bidPrice,bidQty,legA,legB,length):
        product.__init__(self,productID,productName,previousProduct,nextProduct,askPrice,askQty,bidPrice,bidQty)
        self.legA=legA
        self.legB=legB
        self.length=length
