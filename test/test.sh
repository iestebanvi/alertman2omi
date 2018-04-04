echo check ping alive from receiver host
curl -X GET http://127.0.0.1:8000


echo JSON post test message to receiver
curl -X POST -d '{"test": "message"}'  -H 'Content-Type: application/json' http://127.0.0.1:8000/post

echo XML post test message to receiver
curl -X POST -d @testxml.xml -H 'Content-Type: text/xml' http://127.0.0.1:8000/post

echo check ping alive alert2omi
curl -X GET http://127.0.0.1:5000

echo JSON alertmanager json test to alert2omi
curl -X POST -d '{"status": "test", "commonAnnotation" : "anno", "commonLabels": "label"}'  -H 'Content-Type: application/json' http://127.0.0.1:5000/webhook
