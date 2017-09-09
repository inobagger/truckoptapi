from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse, json

import users

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        #self.path
        retD = {} #return dictionary
        recV = dict(urlparse.parse_qsl(parsed_path.query)) #Receive Dictionary
        try:
            email = recV["email"]
            password = recV["password"]
        except KeyError:
            self.send_response(400)
            self.end_headers()
            retD["valid"] = False
            self.wfile.write(json.dumps(retD))
            return
        if("cmd" in recV):
            cmd = recV["cmd"]
        else:
            cmd = None
        if(users.validateUser(email, password)):
            self.send_response(200)
            self.end_headers()
            retD["valid"] = True
        else:
            #Invalid use so we return it with error 403 - Forbidden
            self.send_response(403)
            self.end_headers()
            retD["valid"] = False
            self.wfile.write(json.dumps(retD))
            return
        #The execution follows correctly
        retD["nom"] = users.getNom(email)
        retD["cognom"] = users.getCognom(email)
        retD["telf"] = "+34 682302102"
        retD["direccion"] = users.getDireccion(email)

        if(users.isDriver(email)):
            retD["driver"] = True
            if(cmd == "rutaAcutal"):
                retD["rutaActual"] = users.rutaActual()
            if(cmd == "recogidasPendientes"):
                retD["recogidasPendientes"] = users.recogidasPendientes()

        else:
            retD["driver"] = False
            if(cmd == "verPedidos"):
                retD["pedidos"] = users.getPedidos(email)

        #We return all the info
        self.wfile.write(json.dumps(retD))
        return


if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    ip = '10.201.2.238'
    port = 9001
    server = HTTPServer((ip, port), GetHandler)
    print 'Starting server at http://' + ip + ":" + str(port)
    server.serve_forever()
