# self bu har bir objectni o'zi
class Gm:
    SHIORI="to'lolmasdan o'lib ket"
    def __init__(self,title,engine,price,*args):
        # print('salom')
        self.nomi=title
        self.engine=engine
        self.narx=price
        self.vosita=list(args)

new=Gm('spark',1.2,7000,'rol','balon','kofe')
new2=Gm('onix','1.2 turbo',14000)
new3=Gm('onix','1.2 turbo',14000)
print(new2.__dict__)
print(new.__dict__)
# print(new.narx,new.nomi)
# print(type(new))
# print(new.__dict__)
# print(new.SHIORI)
# print(new2.SHIORI)
# print(new.__dict__)
