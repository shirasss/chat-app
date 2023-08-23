docker build -t  chat-img .
docker run -d --name chat-run -p 5000:5000 chat-img 