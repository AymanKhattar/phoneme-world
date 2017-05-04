# prototype text to phomene fonctionnel mais peu robust 



import nltk
import re

arpabet = nltk.corpus.cmudict.dict()

''' 
Ecrire les phrases a transformer en phoneme dans sentence.txt, 
ATTENTION. finir les phases par un espace, ne fonctionne pas avec 
les mots non presents dans le dictionnaire NLTK
'''

sentence = open("sentence.txt","r").read() 
print sentence
phrase = sentence.split(" ")

arpab = ""
for word in phrase : 
    try:
        phone = arpabet[word][0]
        print "phone = ",phone
    except:
        try:
            counter = 0
            for i in word:
                substring = word[0:1+counter]
                counter += 1
            try:
                for arpa in arpabet[substring][0]:
                    match = re.match(r"([a-z]+)([0-9]+)", arpa, re.I)
                    if match:
                        arpa = match.groups()[0]
                    arpab = arpab + arpa + " "
                arpabe = arpab + " "
            except Exception as e:
                print e
        except Exception as e:
            print e
print sentence, "\n",arpabe


