docker build -t  chat-app .
docker run --name chat -p 8000:5000 chat-app 