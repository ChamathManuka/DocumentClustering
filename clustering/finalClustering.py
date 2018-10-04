import os;

path = os.path.abspath(os.path.dirname(__file__))
f = open(os.path.join(path, 'results\kmeans_clustered_output.txt'), 'rt', encoding='utf-8')
text_file = f.read().split('\n')
count = 0;
F0 = open('zeroCluster.txt', 'w');
F1 = open('firstCluster.txt', 'w');
F2 = open('secondCluster.txt', 'w');
F3 = open('thirdCluster.txt', 'w');
F4 = open('fouthCluster.txt', 'w');
F5 = open('fifthCluster.txt', 'w');
F6 = open('sixthCluster.txt', 'w');
for text in text_file:
    try:
        print(text[0])
        if(text[0] == '0'):
            F0.write(text + '\n')
        elif (text[0] == '1'):
            F1.write(text + '\n')
        elif (text[0] == '2'):
            F2.write(text + '\n')
        elif (text[0] == '3'):
            F3.write(text + '\n')
        elif (text[0] == '4'):
            F4.write(text + '\n')
        elif (text[0] == '5'):
            F5.write(text + '\n')
        elif (text[0] == '6'):
            F6.write(text + '\n')


    except:
        continue;
F0.close()
F1.close()
F2.close()
F3.close()
F4.close()
F5.close()
F6.close()

