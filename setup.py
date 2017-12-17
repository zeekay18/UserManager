import os
import Utilities


print "Building base web server image from Dockerfile\n"

Utilities.createDockFile()

#Build webserver from current directory
Utilities.buildWebServerFromDockFile(os.getcwd())

#pull mongo image from repository
Utilities.pullMongoImage()

#start mongo container
mongoDbContainer = Utilities.startMongodbContainer()

#start web server container and link to mongo db
weberverContainer = Utilities.startWebServer()
weberverContainer.logs()

#log output to window
Utilities.runOutputLogs(mongoDbContainer)