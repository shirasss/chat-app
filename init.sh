docker build -t  chat-img .
docker run --name chat_run -p 8000:5000 chat-img 