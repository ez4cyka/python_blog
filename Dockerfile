FROM ubuntu

COPY . /opt/myblog/

WORKDIR /opt/myblog/

RUN apt-get update

RUN apt-get install -y python3.9 python3-pip
RUN apt-get install -y pkg-config
RUN apt-get install -y libmysqlclient-dev

RUN mkdir ~/.pip && \
    echo "[global]" > ~/.pip/pip.conf && \
    echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple" >> ~/.pip/pip.conf

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3","main.py" ]
