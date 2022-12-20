class Server:
    server_ip = 1

    def __init__(self) -> None:
        self.ip = Server.server_ip
        self.buffer = []
        Server.server_ip += 1

    def get_ip(self):
        return self.ip

    def send_data(self, data):
        Router.buffer.append(data)

    def get_data(self):
        b = self.buffer[:]
        self.buffer.clear()
        return b
        
          

class Router:
    buffer = []
    servers = {}
    
    def link(self, server):
        self.servers[server.get_ip()] = server

    def unlink(self, server):
        self.servers.pop(server.get_ip(), None)

    def send_data(self):
        for d in self.buffer:
            self.servers[d.ip].buffer.append(d)
        self.buffer = []


class Data:
    def __init__(self, data, ip) -> None:
        self.data = data
        self.ip = ip
    

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(msg_lst_from)
print(msg_lst_to)