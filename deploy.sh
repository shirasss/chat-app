#!/bin/bash

# Get the version and commit hash from the user
echo "Enter the version number: "
read version
echo "Enter the commit hash: "
read commit_hash

appname="chat-app"
# Build the Docker image
docker build -t ${appname}:${version} .

# Tag the image with the commit hash
git tag v${version} ${commit_hash}

git push origin v${version}
# Check if the image was pushed successfully
if [ $? -ne 0 ]; then
  echo "Error pushing image to GitHub"
  exit 1
fi

# Success!
echo "Image pushed to GitHub successfully"