"""
    PythonでFTPを行うサンプル.

    Docker Image：
        https://github.com/stilliard/docker-pure-ftpd


docker pull stilliard/pure-ftpd:hardened
docker run -d --name ftpd_server -p 21:21 -p 30000-30009:30000-30009 -e "PUBLICHOST=localhost" stilliard/pure-ftpd:hardened
docker exec -it ftpd_server /bin/bash

pure-pw useradd bob -f /etc/pure-ftpd/passwd/pureftpd.passwd -m -u ftpuser -d /home/ftpusers/bob
Password:  # password


参考：
    http://anon21.qlookblog.net/20091202.html

"""
from ftplib import FTP
from pprint import pprint

ftp = FTP(
    "localhost",
    "bob",
    passwd="password"
)

# ファイルのアップロード
with open("a.txt", "rb") as f:
    ftp.storlines("STOR /aa.txt", f)

# ファイルのアップロード（バイナリー）
with open("b.txt.zip", "rb") as f:
    ftp.storbinary("STOR /bb.zip", f)

# 権限の変更
# ftp.sendcmd("SITE CHMOD 604 /aa.txt")

# ファイルの取得
with open("b.txt", "w") as f:
    ftp.retrlines("RETR /aa.txt", f.write)

# ファイルの取得
with open("bb.txt.zip", "wb") as f:
    ftp.retrbinary("RETR /bb.zip", f.write)

# ディレクトリ作成
ftp.mkd("subdir")

# ファイル一覧の取得
items = ftp.nlst()
pprint(items)

# ファイル一覧を標準出力に表示.
ftp.dir()

items = ftp.mlsd()
for filename, opt in items:
    print("---------------")
    print(filename)
    pprint(opt)

# ディレクトリ削除
ftp.rmd("subdir")














