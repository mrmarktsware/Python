import re

for fname in ['abi_farmer.txt']:

    filename="E:\\Combined\\Processing\\" + fname

    print (fname+"\n")

    f=open(filename,'r')
    thedata=f.read()
    f.close()


    for x in [1]:
        thedata=thedata.replace("	< row id	","")
        thedata=thedata.replace("   "," ")
        tthedata=thedata.replace("  "," ")

        thedata=thedata.replace("|true|","|")
        thedata=thedata.replace("|false|","|")
        thedata=thedata.replace("|null|","|")

        thedata=thedata.replace(" ,",",")
        thedata = thedata.replace(",,",",")
        thedata = thedata.replace(",,",",")
        thedata = thedata.replace(",,",",")
        thedata = thedata.replace('"','')
        thedata = thedata.replace('@ ','@')
        thedata = thedata.replace(' @','@')
        thedata=thedata.replace('[tag]','|')
        thedata=thedata.replace('[TAG]','|')
        thedata=thedata.replace("c://temp//adr//address//part ","")
        thedata=thedata.replace("c://temp//adr//address//part|address|mdb|original data copy","")

        thedata=thedata.replace("c:\\temp\\adr\\address\\error\\new folder (2)\\master addresse2.mdb","")
        thedata=thedata.replace("c://temp//adr//address//error//new folder//master addresses.mdb","")
        thedata=thedata.replace("original data copy","")
        thedata=thedata.replace(",x|","|")
        thedata=thedata.replace("c:/temp/adr/address/part","")
        thedata=thedata.replace("address|mdb","")
        thedata=thedata.replace("]:","")

        thedata = re.sub(r"[ @,-_][|]", "|", thedata)
        thedata = re.sub(r"[|][ @,-_]", "|", thedata)
        thedata=thedata.replace("|/n","/n")


        thedata = re.sub(r"[|][,][0-9]\n", "\n", thedata)
        thedata = re.sub(r"[|@, ]\n", "\n", thedata)
        thedata = re.sub(r"[|][0-9]\n", "\n", thedata)
        thedata = re.sub(r"[|][0-9][0-9]\n", "\n", thedata)
        thedata = re.sub(r"[@][0-9]\n", "\n", thedata)
        thedata = re.sub(r"[@][0-9][0-9]\n", "\n", thedata)

        thedata = re.sub(r"[|][0-9][0-9][|]", "|", thedata)
        thedata = re.sub(r"[|][0-9][|]", "|", thedata)

        thedata = re.sub(r"[_][0-9][0-9][_]", "|", thedata)
        thedata = re.sub(r"[_][0-9][_]", "|", thedata)

        thedata = re.sub(r"\][:][0-9][0-9][0-9][0-9][0-9][0-9][|]", "|", thedata)

        # 19:14:33:2385
        thedata = re.sub(r"[0-9][0-9]:[0-9][0-9]:[0-9][0-9]:[0-9][0-9][0-9][0-9]", "|", thedata)
        thedata = re.sub(r"[0-9][0-9][0-9][0-9]:[0-9][0-9]", "|", thedata)

        #thedata = re.sub(r"[0-9][0-9]:[0-9][0-9]:[0-9][0-9][0-9]:[0-9][0-9][0-9][0-9]", "|", thedata)
        #thedata = re.sub(r"[0-9][0-9]:[0-9][0-9][0-9][0-9]", "|", thedata)
        #thedata = re.sub(r"[0-9][0-9][0-9][0-9][0-9].[0-9][0-9]", "|", thedata)
        #thedata = re.sub(r"[0-9][0-9]\\[0-9][0-9]\\[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9][0-9]", "|", thedata)

        #thedata = re.sub(r"\/[0-9]\/[0-9][0-9][0-9][0-9] [0-9][0-9]:[0-9][0-9]:[0-9]", "|", thedata)
        #thedata = re.sub(r"[:][0-9][0-9][0-9][0-9][0-9][0-9][0-9][|]", "|", thedata)
        #thedata = re.sub(r"[|][0-9][0-9][0-9][@][,][|]", "|", thedata)
        #thedata = re.sub(r"/][:][0-9][0-9][0-9][0-9][0-9][0-9][0-9][,]", "|", thedata)
        #thedata = re.sub(r"[0-9][0-9][0-9]:[0-9][0-9]", "|", thedata)
        #thedata = re.sub(r"[0-9]", "|", thedata)
        #thedata = re.sub(r"[0-9]", "|", thedata)
        #thedata = re.sub(r"[0-9]", "|", thedata)

        #thedata=thedata.replace("| |","|")
        #thedata=thedata.replace("||||","|")
        #thedata=thedata.replace("|||","|")
        #thedata=thedata.replace("||","|")
        #thedata=re.sub(r"[:,| ][:,| ][:,| ][:,| ]","|",thedata)

        #thedata=thedata.replace("||:|","|")
        #thedata=thedata.replace("]:|","|")
        #thedata=thedata.replace("copy of girlies.mdb","|")

        #thedata=thedata.replace("|,","|")
        #thedata=thedata.replace("null","|")
        #thedata=thedata.replace("]|","|")
        #thedata=thedata.replace("  "," ")
        #thedata=thedata.replace("__","_")
        #thedata=thedata.replace("@|","|")
        #thedata=thedata.replace("|@","|")
        #thedata=thedata.replace(".|","|")
        #thedata=thedata.replace("|.","|")
        #thedata=thedata.replace("||","|")


        thedata=thedata.replace("\n@","\n")
        thedata = thedata.replace("\n,", "\n")
        thedata = thedata.replace("\n ", "\n")
        thedata = thedata.replace("\n.", "\n")
        thedata = thedata.replace("\n_", "\n")
        thedata = thedata.replace("\n-", "\n")
        thedata = thedata.replace("\n|", "\n")

        thedata=thedata.replace("|x\n","\n")
        thedata=thedata.replace("|\n","\n")
        thedata=thedata.replace("_\n","\n")
        thedata = thedata.replace(",x|", "|")



    f=open(filename+"cleaned",'w')
    f.write(thedata)
    f.close()