from livereload import Server

server = Server()
server.watch("*.html")
server.watch("static/*.css")
server.watch("static/*.js")
server.serve()
