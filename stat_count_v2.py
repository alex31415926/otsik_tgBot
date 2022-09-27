import os
import pprint
import config_stat
from sys import argv

#results_data_patch = r"e:\_py\bots\_MariBot\results"
results_data_patch = config_stat.results_data_patch
result_file = config_stat.result_file
content = os.listdir(results_data_patch)
print(content)

shkala1Q = [1, 9, 17, 25, 33, 41]
shkala2Q = [2, 10, 18, 26, 34, 42]
shkala3Q = [3, 11, 19, 27, 35, 43]
shkala4Q = [4, 12, 20, 28, 36, 44]
shkala5Q = [5, 13, 21, 29, 37, 45]
shkala6Q = [6, 14, 22, 30, 38, 46]
shkala7Q = [7, 15, 23, 31, 39, 47]
shkala8Q = [8, 16, 24, 32, 40, 48]
invertQ = [5, 10, 12, 13, 18, 24, 25, 36, 27, 31, 33, 35, 47]


sc1, sc2, sc3, sc4, sc5, sc6, sc7 = 0, 0, 0, 0, 0, 0, 0
#scales = [sc1, sc2, sc3, sc4, sc5, sc6, sc7]
scales_results = []
results = []

minAge = 10 #argv[1]
maxAge = 32 #argv[2]
sex = "w" #argv[3]
role = "role_5"

print(f"{minAge} {maxAge} {sex}")

for fileName in content:
    if fileName[0].isdigit:
        match = True
        file = open(results_data_patch+"/"+fileName, 'r')
        fileData = file.read().split('\n')
        dataLine = fileData[0]
        fileSex, fileAge, fileRole = fileData[2], int(fileData[4]), fileData[3]

        str2 = []

        for char in dataLine:
            if char.isdigit():
                str2.append(int(char))

        if not minAge <= fileAge <= maxAge:                 # перенести все проверки в отдельную функцию
            #print(f"возраст {fileAge} не подходит ({minAge} {maxAge})")
            match = False
        if not sex == fileSex:
            print(f"пол {fileSex} не подходит ({sex})")
            match = False
        if not role == fileRole:
            print(f"роль {fileRole} не подходит ({role})")
            match = False

        if match:
           results.append(str2)


#print(f"прошедших {len(results)}, не прошедших {nomatch}")
goodResults = []
for result in results:              #проверка целостности данных
    #result = result.strip("]")
    #result = result.rstrip("]")
    if len(result) != 48:
        print("Data broken")
    else:
        print(result)
        goodResults.append(result)

def check_result(resultsData):
    sc1, sc2, sc3, sc4, sc5, sc6, sc7 = 0, 0, 0, 0, 0, 0, 0
    scales = [sc1, sc2, sc3, sc4, sc5, sc6, sc7]
    index = 1
    #print(resultsData)

    def replaceAnswer(answer):
            if answer == 5:
                return 1
            elif answer == 4:
                return 2
            elif answer == 3:
                return 3
            elif answer == 2:
                return 4
            elif answer == 1:
                return 5

    for answer in resultsData:
        if index in invertQ:
            answer = replaceAnswer(answer)

        if index in shkala1Q:
            scales[0] += answer
        elif index in shkala2Q:
            scales[1] += answer
        elif index in shkala3Q:
            scales[2] += answer
        elif index in shkala4Q:
            scales[3] += answer
        elif index in shkala5Q:
            scales[4] += answer
        elif index in shkala6Q:
            scales[5] += answer
        elif index in shkala7Q:
            scales[6] += answer
        #elif index in shkala8Q:
            #[scales][7] += answer
        index += 1
    print
    return scales

for goodResult in goodResults:
     scales_results.append(check_result(goodResult))

pprint.pprint(scales_results)


scalesDCstats = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
mechDCstats = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

def count_scales_stats(scales_results):
    for result in scales_results:
        for num in range(6):
            if result[num] < 12:
                scalesDCstats[num][0] += 1
            elif result[num] > 24:
                scalesDCstats[num][1] += 1

def count_mech_stats(scales_results):
    for result in scales_results:
        sh1 = result[0]
        sh2 = result[1]
        sh3 = result[2]
        sh4 = result[3]
        sh5 = result[4]
        sh6 = result[5]
        sh7 = result[6]

        samoopredmechivanie = (sh1 + sh2 + sh3 + sh7) / 4
        samootsenivanie = (sh4 + sh6 + sh3 + sh7) / 4
        samoformirovanie = (sh1 + sh5 + sh3 + sh7) / 4
        samootojdestvlenie = (sh1 + sh2 + sh4 + sh6) / 4
        samopredyavlenie = (sh1 + sh5 + sh1 + sh2) / 4
        samoodobrenie = (sh1 + sh5 + sh4 + sh6) / 4

        mechs = [samoopredmechivanie, samootsenivanie, samoformirovanie,
        samootojdestvlenie, samopredyavlenie, samoodobrenie]

        for mech, num in zip(mechs, range(5)):
            if mech < 12:
                mechDCstats[num][0] +=1
            elif mech > 24:
                mechDCstats[num][0] +=1


count_scales_stats(scales_results)
count_mech_stats(scales_results)
#заменить путь или перенести в конфиг
#result_file = r"e:\_Denver\denwer\www\denwer\bot\stat"

with open(result_file, 'w') as file:
    file.write(f"{str(len(goodResults))}\n")
    for result in scalesDCstats:
            file.write(f"{result[0]} {result[1]}\n")
    for result in mechDCstats:
            file.write(f"{result[0]} {result[1]}\n")

pprint.pprint(scalesDCstats)
pprint.pprint(mechDCstats)





