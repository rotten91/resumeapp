from flask import Flask

app = Flask(__name__,static_folder="E:\\resumeapp\\esumeapp\\static")

import resumeapp.views
