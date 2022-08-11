# read pdf from file and code(md5),then save to DB as MD5 and binary(File_pdf)
#2022-8-7
#BINSKIN
import sqlite3
import os
import hashlib



if __name__ == '__main__':
    conn = sqlite3.connect("./DB/ZhengCG.db")
    cur = conn.cursor()
    row = cur.execute("SELECT ID,URL,MD5 FROM HMCINFO;")
    workList = []
    for item in row:
        if item[2] == None and item[1] != None:
            record = {'ID':item[0],'URL':item[1].replace('/', '\\')}
            workList.append(record)
            # print(record)
    md5List = []
    for i in workList:
        try:
            hash_md5 = ''
            pdfFile = open(i.get('URL'),"rb")
            pdfBinary = pdfFile.read()
            hash_md5 = (hashlib.md5(pdfBinary).hexdigest())
            pdfFile.close()
        except:
            print("open pdf ERROR",i.get('ID'),'###',i.get('URL'))
        #文件读取成功
        if hash_md5 != '':
            cur.execute("UPDATE HMCINFO SET MD5 = ? WHERE ID = ?", (hash_md5, i.get('ID')))
            conn.commit()
            print("UPDATE : ",i.get('ID'))
            if hash_md5 not in md5List:
                if (len(list(cur.execute("SELECT ID FROM HMCFILE WHERE MD5 = ? ", (hash_md5,))))) == 0:
                    cur.execute("INSERT  INTO HMCFILE VALUES(?,?,?)", (None, hash_md5, pdfBinary))
                    md5List.append(hash_md5)
                    conn.commit()
        #pdfFile = open(, "rb")
        #pdf_binary = pdfFile.read()
        #pdfFile.close()
        #print(hashlib.md5(pdf_binary).hexdigest())
        #id = id + 1
        #cur.execute("INSERT INTO PDFTestFile VALUES (?,?,?)", (id, hash_md5, pdf_binary))
        #data = cur.fetchone()
    #conn.commit()
    conn.close()