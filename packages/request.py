###############################################################################################################
# script:       request.py
# description:  This script send the request to the server and analize the response
# version:      1.1
# creation:     December 2, 2023
# update:       January 2, 2023
###############################################################################################################
# Library/(ies)
import requests
import os
import threading
import subprocess
import time
import packages.error as error

OPTIONS = {
    "e"    : " -e ",                                      # environment
    "n"    : " -n ",                                      # iterations
    "tr"   : " --timeout-request ",                       # the time (in milliseconds) to wait for requests to return a response
    "ts"   : " --timeout-script ",                        # the time (in milliseconds) to wait for scripts to return a response
    "d"    : " -d ",                                      # specific csv or json
    "x"    : " -x ",                                      # do not care if the tests fails
    "k"    : " -k ",                                      # disable SSL
    "f"    : " --folder ",                                # specific folder
    "html" : " -r htmlextra --reporter-htmlextra-export " # html report
}

class request:
    def __init__(self):
        self.path        = os.getcwd();
        self.command     = "newman run"
        self.collection  = self.path + "/src/collection"
        self.environment = self.path + "/src/environment"
        self.reports     = self.path + "/reports/"
        self.options     = []
        self.report      = False
    
    def set_collection(self, collection):
        self.collection = collection
        
    def set_environment(self, environment):
        self.environment = environment
          
    def set_options(self, options):
        # it must be ["option", "value"]
        self.options = options
                
    def build_request(self):
        try:
            self.command = "newman run " + self.collection
            for option in self.options:
                if(option[0] == "html"):
                    option[1] = OPTIONS[option[0]] + self.reports
                    self.report = True
                if(option[0] == "e"):
                    option[1] = self.environment
                self.command = self.command + OPTIONS[option[0]] + option[1]
        except:
            error.popup_showerror("9")
    
    def send_request(self):
        if(self.report):
            self.request_threads()
            self.report_threads()
        else:
            self.request_threads()
    
    def send_command(self):
        os.system(self.command)
        
    def request_threads(self):
        no_main_thread = threading.Thread(target=self.send_command, name='no_main_thread')
        no_main_thread.start()
        no_main_thread.join()

    def report_threads(self):
        no_main_thread = threading.Thread(target=self.open_browser, name='open_browser_thread')
        no_main_thread.start()

    def open_browser(self):
        try:
            url = self.validate_url(self.get_last_file())
            url = self.reports + url
            chrome_command = "open -a 'Google Chrome' {}".format(url)
            subprocess.run(chrome_command, shell=True)
        except:
            return ["6"]
        
    def validate_url(self, url):
        extension = url[len(url) - 4: len(url)]
        if(extension == "html"):
            return url
        else:
            return ["6"]
        
    def get_last_file(self):
        # Obtener la lista de archivos en la carpeta
        files = os.listdir(self.reports)
        # Filtrar solo los archivos (no directorios) y obtener la fecha de creación de cada archivo
        all_files = [(file, os.path.getctime(os.path.join(self.reports, file))) for file in files if os.path.isfile(os.path.join(self.reports, file))]
        # Ordenar la lista de archivos por fecha de creación en orden descendente
        all_files.sort(key=lambda x: x[1], reverse=True)

        # Obtener el último archivo creado
        if all_files:
            last_file = all_files[0][0]
            return last_file
        else:
            return ["6"]    
