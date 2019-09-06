import py2neo
import pymysql
import json
from py2neo import Graph, Node, Relationship


class Graphshare():

    def __init__(self):
        self.db = pymysql.connect("192.168.0.200", "zrj", "", "samplefamily", charset="UTF8")
        self.graph = Graph(host="localhost", auth=("neo4j", "xebszw7lllg"))
        self.virussample = 'virus_family.json'

    def get_hashnode(self):
        cursor = self.db.cursor()
        cursor.execute("select Sample_HASH from virus_family")
        hashdata = cursor.fetchall()
        return hashdata

    def get_familyname(self):
        cursor = self.db.cursor()
        cursor.execute("select * from virus_family")
        familydata = cursor.fetchall()
        return familydata

    def insert_samplename_node(self):
        allname = self.get_hashnode()
        for row in allname:
            hashnode = Node('Sample_name', name=row[0])
            self.graph.create(hashnode)

    def insert_familyname_node(self):
        allname = self.get_familyname()
        for row in allname:
            for i in range(1,74):
                if row[1]==None:
                    continue
                else:
                    a=len(self.graph.nodes.match('Family_name', name=row[i]))
                    if a>=1:
                        continue
                    else:
                        familynode=Node('Family_name',name=row[i])
                        self.graph.create(familynode)

    def insert_relation(self):
        allrelation=self.get_familyname()
        for row in allrelation:
            for i in range(1,74):
                samplename=self.graph.nodes.match('Sample_name',name=row[0]).first()
                if row[i]==None:
                    continue
                else:
                    familyname=self.graph.nodes.match('Family_name',name=row[i]).first()
                    rela=Relationship(samplename,'family',familyname)
                    self.graph.create(rela)

    def run(self):
        # self.insert_samplename_node()
        # self.insert_familyname_node()
        self.insert_relation()

def main():
    gra = Graphshare()
    gra.run()

if __name__ == '__main__':
    main()
