
TESTLINK
curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-testlink/master/docker-compose.yml > docker-compose.yml
docker-compose up -d

user
bitnami
API Key: e71ffdb42d75bfda8617aebaf6b11274


JENKINS
docker run --rm -d -u root -p 8081:8080 -v jenkins-data:/var/jenkins_home jenkinsci/blueocean

admin
admin

docker inspect <Testlink_container_id> | grep "IPAddress"