import os
import Utilities


print "Building base web server image from Dockerfile\n"

Utilities.createDockFile()

#Build webserver from current directory
Utilities.buildWebServerFromDockFile(os.getcwd())

#pull mongo image from repository
#Utilities.pullMongoImage()

#start mongo container
Utilities.startMongodbContainer()

#start web server container and link to mongo db
Utilities.startWebServer()

#log out to window
Utilities.runOutputLogs()