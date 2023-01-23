FROM python:3.9

# set the working directory
WORKDIR /app

# start the container in interactive mode
CMD ["bash"]

# set the entrypoint
ENTRYPOINT ["/bin/bash", "-c"]