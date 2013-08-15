import os

def clean_folder(folder):
  for file in os.listdir(folder):
    path = os.path.join(folder,file)
    if os.path.isdir(path):
        clean_folder(path)

    if '.pyc' == file[-4:]:
        print 'deleting: ' + str(path)
        os.remove(path)

if __name__ == '__main__':
  folder = '/Users/feaver/Google Drive/Uni/2013/COMP556/Assignment 1/workspace/Assignment 1/src'
  clean_folder(folder)