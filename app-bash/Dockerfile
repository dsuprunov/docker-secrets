FROM bash:latest

CMD printf 'Docker Compose / File\n'; \
		export FILE_LOGIN=$(cat /run/secrets/file_login); printf "\tLogin: $FILE_LOGIN\n"; \ 
		export FILE_PASSWORD=$(cat /run/secrets/file_password); printf "\tPassword: $FILE_PASSWORD\n"; \
		printf "\n";

