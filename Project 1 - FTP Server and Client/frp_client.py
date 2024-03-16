import ftplib
import os
import sys
from colorama import init, Back, Fore
from abc import ABC, abstractmethod

init(autoreset = True)

class client(ABC):
    def __init__(self, server_to_connect):
        self.__server_to_connect = server_to_connect
    
    @property
    def server_ip(self):
        return self.__server_to_connect
    
    @abstractmethod
    def connect_to_server(self):
        pass

class ftp_client(client):
    def __init__(self,server_to_connect):
        super().__init__(server_to_connect)
        self.__files_on_server = []
        self.__files_on_local_system = self.read_local_files()
        self.connect_to_server()
        self.populate_server_files_list()
        self.__file_difference = self.compare_remote_local

    def connect_to_server(self):
        self.ftp_session = ftplib.FTP(self.server_ip)
        self.ftp_session.login("anonymous", "")
    
    def read_local_files(self):
        return os.listdir("./files")
    
    def populate_server_files_list(self):
        temp = []
        self.ftp_session.dir(temp.append)
        for _ in range(0, len(temp)):
            self.__files_on_server.append(temp[_].split(" ")[-1])
        del temp
                            
    @property
    def display_files_on_server(self):
        return self.__files_on_server
    
    @property
    def display_files_on_local(self):
        return self.__files_on_local_system
    
    @property
    def compare_remote_local(self):
        return list(set(self.__files_on_server) - set(self.__files_on_local_system))

    @property
    def get_difference(self):
        if any(self.compare_remote_local): return self.__file_difference
        else: 
            self.__file_difference.append("All up to date")
            return self.__file_difference
    
    def download_difference(self):
        if "All up to date" in self.__file_difference:
            pass
        else:
            for _ in self.__file_difference:
                self.ftp_session.retrbinary("RETR " + _ , open("./files/{}".format(_), 'wb').write)
                print(Back.GREEN + Fore.BLACK + "\nFile downloaded: " + _)
        self.update_lists()
    
    def update_lists(self):
        self.__files_on_local_system = []
        self.__files_on_local_system = self.read_local_files()
        self.__files_on_server = []
        self.populate_server_files_list()
        self.__file_difference = self.compare_remote_local
             
ftp_client_instance = ftp_client("127.0.0.1")

while True:
    print('''
          1: List locally stored files\n
          2: List remotely stored files\n
          3: Files on remote server but not local server\n
          4: Download files\n
          5: Exit
          ''')
    cmd = input("Choose option: ")
    
    match cmd:
        case "1": print("\n", *ftp_client_instance.display_files_on_local)
        case "2": print("\n", *ftp_client_instance.display_files_on_server)
        case "3": print("\n", *ftp_client_instance.get_difference)
        case "4": ftp_client_instance.download_difference()
        case "5": sys.exit()