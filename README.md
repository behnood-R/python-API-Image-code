This project aims to fulfill the following requirements related to the application side and network structure. 
Firstly, the API should be written in Python and should accept an image and return image metadata, including dimensions, encoding, and compression. 
Secondly, the API should log all database POST requests with timestamps and IP addresses. 
Thirdly, an API endpoint that accepts an image and returns the results as JSON should be created. 
Fourthly, the API should be packaged in a Docker image along with all configuration files and should be deployed in the cloud. 
Fifthly, the API should be able to be deployed on any other AWS accounts. 
Finally, the implementation should be fully automated and should include Dockerfiles and documentation.

For the application side, a Python-based API has been used to meet the abovementioned requirements. 
The API is written in Python and listens to port 8888. Gunicorn is a WSGI server to manage API calls and listen to port 8000. 
The application is containerized, and the image is available on DockerHub. 
Nginx is installed on top of Gunicorn to act as a load balancer and reverse proxy. 
The API responds in JSON format, and the scripts and Dockerfile are available on GitHub.

https://github.com/behnood-R/python-API-Image-code.git


For the network structure, a VPC, a public and a private subnet, an internet gateway, a NAT gateway, an elastic IP, and route tables for public and private subnets are included. 
A security group is used to open traffic on specific ports and all traffic from inside to the internet. 

The whole implementation stages have been automated in Terraform, and all related scripts are available on GitHub.

https://github.com/behnood-R/image-upload-deployment-terraform-nginx.git

As a potential improvement plan, Kubernetes can be used for the production stage, including the EC2 cluster behind a load balancer and passing the traffic to the load balancer via Route53. 
This way, SSL can be implemented to secure the API. Additionally, an API gateway may help with higher loads. Nginx logs can be shipped into ELK for further investigation.

To run the Terraform script, the User should create and download a Key, and the path to the Key should be updated on lines 4 and 5 in the script. 
The User has to create related AIM users and credentials beforehand. As all free tire services are used, it may take up to 3 minutes for the API to be ready to accept calls.

Example of the response in Postman application has been included in Github :

https://github.com/behnood-R/python-API-Image-code/blob/main/Screenshot%202023-03-29%20at%2010.18.38.png

