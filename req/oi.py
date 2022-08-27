import http.client


conn = http.client.HTTPConnection("localhost:8080")


payload = "{\"titulo\":\"Duvida Postman\",\"mensagem\":\"Texto da mensagem\",\"nomeCurso\":\"Spring Boot\"}"


headers = {



    'header': "content-type: application/json"

}


conn.request("POST", "/topicos", payload, headers)
res = conn.getresponse()

data = res.read()


print(data.decode("utf-8"))
