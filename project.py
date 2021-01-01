import dropbox
import shutil
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token      

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'n_lUHFKbTkYAAAAAAAAAASazgjx6xOYxcKKhCJqrxzW6O7mJsFpzPIq9oQ0yGn4k'
    transferData = TransferData(access_token)
    path = '/Users/vivekkumar/Documents/python_projects/proj-c101'
    folder = 'test'
    dat = os.walk(path)
    for i in dat:
        data = i
        file_ = str(data[0])
        newPath = os.path.join(folder,file_)
        AllFiles = os.listdir(newPath)

    for i in AllFiles:
        file_from = newPath+'/'+i
        file_to = '/'+i
        transferData.upload_file(file_from,file_to)
        print("Files uploaded")
        

if __name__ == '__main__':
    main()