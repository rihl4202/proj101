import dropbox
class Transfer:
    def __init__(self,token):
        self.token = token
    def upload(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.token)
        with open(fileFrom,"rb") as f:
            dbx.files_upload(f.read(),fileTo)
data = Transfer("sl.BC-ayw22VzLHEP3SYWyy7lh1NJctDiXg1jKJFcFE4gAcHxhzgOxt7IQ60tTpVPhkKOJuUwp88Iol42uGmmLQcU63aazuSKtN5q97Jm3Q30UDqiVqCX3ZT-TbVsVeXXC6ToJ6NM8")
fileFrom = input("Enter your source path: ")
fileTo = input("Enter your destination path: ")
data.upload(fileFrom,fileTo)
print("Files have moved.")