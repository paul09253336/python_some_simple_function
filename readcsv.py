        listECG = []
        listPRE = []
        listPPG = []
        listBOD = []
        listnum = []
        i = 0
        k=0
        with open(fileName, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                #print(row)
                i = i + 1
                listECG.append(row[1])
                listPRE.append(row[2])
                listPPG.append(row[3])
                listBOD.append(row[4])
                listnum.append(i)
        y_ECG = listECG
        y_PRE = listPRE
        y_PPG = listPPG
        y_BOD = listBOD
        x = listnum