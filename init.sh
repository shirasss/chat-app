docker volume create chat-app-data
docker build -t  chat-app:v0.0.0 .
# docker run --name chat-run -p 5000:5000 chat-app 
docker run -v chat-app-data:/chatApp/data -p 5000:5000 --name chat-run chat-app:v0.0.0