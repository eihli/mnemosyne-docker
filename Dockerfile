FROM python:3.10.6-bullseye
MAINTAINER Eric Ihli <eihli@owoga.com>
RUN apt-get update
RUN apt-get install -y texlive vim sqlite3
RUN pip3 install --upgrade pip
RUN pip3 install matplotlib cheroot webob argon2-cffi cherrypy matplotlib sphinx pyqt5 pyqtwebengine nose decorator
WORKDIR /opt
RUN git clone https://github.com/mnemosyne-proj/mnemosyne.git
WORKDIR /opt/mnemosyne
RUN python3 setup.py install
COPY config.py /root/.config/mnemosyne/config.py
WORKDIR /
CMD ["mnemosyne --web-server --sync-server"]
