# Run a Mnemosyne web & sync server in a Docker container

`generate_password.py` requires `argon2-cffi`.

``` sh
pip3 install --user argon2-cffi
python3 generate_password.py <username> <password>
docker build -t mnemosyne .
docker-compose up
```
