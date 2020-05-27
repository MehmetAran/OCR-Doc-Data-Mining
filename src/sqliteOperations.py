
import sqlite3
import os
class SqliteOperations:
    basePath = ""
    conn = None
    def __init__(self):
        self.basePath = os.path.abspath('.')
        self.conn = sqlite3.connect(self.basePath + '/resource/db/sql.db')

    def insert(self,documentName,pageNumber,indexName,leftText,rightText,topText,bottomText):
        c = self.conn.cursor()
        c.execute("INSERT INTO Documents(documentName,pageNumber,indexName,leftText,rightText,topText,bottomText) VALUES (?,?,?,?,?,?,?)",
        (documentName,pageNumber,indexName,leftText,rightText,topText,bottomText))
        self.conn.commit()

    def delete(self,id):
        c = self.conn.cursor()       
        c.execute("DELETE from Documents where id =?",(id,))
        self.conn.commit()
    def deleteFromTargetDocuments(self,id):
        c = self.conn.cursor()       
        c.execute("DELETE from TargetDocuments where id =?",(id,))
        self.conn.commit()

    
    def updateFromTargetDocuments(self,id,documentName,targetDocument):
        c = self.conn.cursor()        
        c.execute("UPDATE  TargetDocuments SET documentName=?,targetDocument=? where id = ?",
        (documentName,targetDocument,id))
        self.conn.commit()

    def update(self,id,documentName,pageNumber,indexName,leftText,rightText,topText,bottomText):
        c = self.conn.cursor()        
        c.execute("UPDATE  Documents SET documentName=?,pageNumber=?,indexName=?,leftText=?,rightText=?,topText=?,bottomText=? where id = ?",
        (documentName,pageNumber,indexName,leftText,rightText,topText,bottomText,id,))
        self.conn.commit()

    
    def getAll(self):
        c = self.conn.cursor()
        c.execute("select * from Documents")
        documents = c.fetchall()
        self.conn.commit()
        return documents;
    
    def findOneFromDocument(self,documentId):
        c = self.conn.cursor()
        c.execute("select * from Documents where documentID=?",(documentId,))
        document = c.fetchone()
        self.conn.commit()
        return document;

    def findByDocumentName(self,documentName):
        c = self.conn.cursor()

        c.execute("select * from Documents where documentName=?",(documentName,))
        documentIndexes =      documents = c.fetchall()
        self.conn.commit()
        return documentIndexes

    def findByDocumentNameFromTargetDocuments(self,documentName):
        print(documentName)
        c = self.conn.cursor()
        c.execute("select * from TargetDocuments where documentName=?",(documentName,))
        document = c.fetchone()
        self.conn.commit()
        return document

    def insertTargetDocument(self,documentName,targetDocument):
        print(documentName,",",targetDocument)
        c = self.conn.cursor()
        c.execute("INSERT INTO TargetDocuments(documentName,targetDocument) VALUES (?,?)",
        (documentName,targetDocument))
        self.conn.commit()

"""

a = SqliteOperations().findByDocumentNameFromTargetDocuments("YÜKSEK LİSANS TEZ KONUSU BİLDİRİM FORMU")

print(a)"""
"""
a = SqliteOperations()
a.insert("mehmet",1,"deneme1","deneme2","deneme3","deneme4","deneme5")
a.update(10,"1",1,"1","1","1","1","1")
a.delete(15)
results = a.findByDocumentName("1")
for result in results:
    print(result)
results = a.getAll()
for result in results:
    print(result)"""