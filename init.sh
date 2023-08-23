docker build -t  chat-img .
docker run -d --name chat_run -p 8000:5000 chat-img 