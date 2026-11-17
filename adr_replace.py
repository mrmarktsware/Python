import re



def process(filepath):

    print ('Processing ' & filename)


    with open(filepath, 'r') as file:
        data = file.read()
        data = data.replace(' :',':')
        data = data.replace(': ',':')
        data = data.replace('|1|','|')
        data = data.replace('|0|','|')
        data = data.replace(' ,',',')
        data = data.replace('  ',' ')
        data = data.replace('@@','@')
        data = data.replace('||','|')
        data = data.replace(': ', ':')

        p=re.compile('[:][0-9][0-9][0-9][0-9][0-9][0-9][0-9][|]')
        data=re.sub(p,'',data)

        p=re.compile('[:][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][|]')
        data=re.sub(p,'',data)

        p=re.compile('[0-9][0-9][:][0-9][:][0-9][:][0-9][:][0-9][0-9]')
        data=re.sub(p,'',data)

        p=re.compile('[0-9][0-9][:][0-9][:][0-9][:][0-9][0-9][:][0-9][0-9]')
        data=re.sub(p,'',data)

        p=re.compile('[0-9][0-9][:][0-9][:][0-9][0-9][:][0-9][:][0-9][0-9]')
        data=re.sub(p,'',data)

        p=re.compile('[0-9][0-9][0-9][:][0-9][:][0-9][0-9][0-9][|]')
        data=re.sub(p,'',data)

        p=re.compile('[|][0-9][0-9][0-9][|]')
        data=re.sub(p,'',data)

        p=re.compile('[|][0-9][0-9][|]')
        data=re.sub(p,'',data)

        p=re.compile('[|][0-9][|]')
        data=re.sub(p,'',data)

        p=re.compile('[\n][0-9][0-9][0-9][0-9][0-9][0-9][|]')
        data=re.sub(p,'\n',data)

        p=re.compile('[\n][0-9][0-9][0-9][0-9][0-9][|]')
        data=re.sub(p,'\n',data)

        p=re.compile('[\n][0-9][0-9][0-9][0-9][|]')
        data=re.sub(p,'\n',data)

        p=re.compile('[\n][0-9][0-9][0-9][|]')
        data=re.sub(p,'\n',data)

        p=re.compile('[\n][0-9][0-9][|]')
        data=re.sub(p,'\n',data)

        p=re.compile('[\n][0-9][|]')
        data=re.sub(p,'\n',data)


        p=re.compile('[\n][| ;,-_]')
        data=re.sub(p,'\n',data)

        p=re.compile('[/[][/[]]')
        data=re.sub(p,'\n[',data)


        p=re.compile('[| @:,][\n]')
        data=re.sub(p,'\n',data)

        p=re.compile('[|][0-9][0-9][0-9][:][0-9][:][0-9][0-9][0-9][\n]')
        data=re.sub(p,'|\n',data)


        p=re.compile('[0-9][0-9][:][0-9][0-9][:][0-9][:][0-9][0-9][:][0-9][0-9][:][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
        data=re.sub(p,'|',data)


        p=re.compile('[0-9][0-9][0-9][0-9][:][:][0-9][0-9][0-9][0-9]')
        data=re.sub(p,'|',data)


        p=re.compile('[|][0-9][0-9][0-9][0-9][0-9][0-9][0-9][\n]')
        data=re.sub(p,'|\n',data)


    with open(filepath, 'w') as file:
        file.write(data)

process('E:\\ABI_FARMER.TXT')

print("Text replaced")