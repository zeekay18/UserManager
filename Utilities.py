import docker

lowLevelClient = docker.APIClient()  #To access low level functions
client = docker.from_env()


def createDockFile():
    print "creating Dockerfile\n"

    file = open("Dockerfile", "w")
    file.write("FROM node:latest\n\n")
    file.write("ADD package.json /tmp/package.json\n\n")
    file.write("RUN cd /tmp && npm install\n\n")
    file.write("RUN mkdir /app && cp -a /tmp/node_modules /app \n\n")
    file.write("WORKDIR /app\n\n")
    file.write("ADD . /app\n\n")
    file.write("EXPOSE 3000\n\n")
    file.write("CMD [ \"npm\", \"start\" ]\n\n")
    file.close()

    print "Dockerfile created\n"


def buildWebServerFromDockFile(filePath):
    print "building weserver image..."
    try:
        for line in lowLevelClient.build(
                path=filePath, decode=True, tag="web_server"):
            print line
        print "webserver image built."
    except docker.errors.BuildError as error:
        print error


def pullMongoImage():
    for line in lowLevelClient.pull('mongo', stream=True, decode=True):
        print line


def startMongodbContainer():
    mongodbContainer = client.containers.run(
        'mongo',
        name="mongodb",
        ports={'27017/tcp': 27017},
        volumes={'/data/db/': {
            'bind': '/data/db',
            'mode': 'rw'
        }},
        detach=True,
        remove=True)
    return mongodbContainer


def startWebServer():
    webServerContainer = client.containers.run(
        "web_server",
        name="web",
        ports={'3000/tcp': 3000},
        links={'mongodb': 'mongodb'},
        remove=True,
        detach=True)
    return webServerContainer


def runOutputLogs(container):
    for line in container.attach(stdout=True, stderr=True, stream=True):
        print line
