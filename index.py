from flask import Flask, render_template, request, jsonify
import copy
app = Flask(__name__)


T = []
twoDimentWorkedList = []


def toTwoDimentionalList(workedList):
	resultList = []
	j = 0
	k = 0
	for i in range(len(workedList)):
		if (k == 9):
			return resultList
		if(j == 9):
			j = 0
			k += 1
		if(j == 0):
			resultList.append([])

		resultList[k].append(workedList[i])
		j += 1
	return resultList


def possible(y, x, n):
	global twoDimentWorkedList
	for i in range(0, 9):
		if twoDimentWorkedList[y][i] == n:
			return False
	for i in range(0, 9):
		if twoDimentWorkedList[i][x] == n:
			return False
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(0, 3):
		for j in range(0, 3):
			if twoDimentWorkedList[y0 + i][x0 + j] == n:
				return False
	return True


def solve():
	global T, twoDimentWorkedList
	for y in range(9):
		for x in range(9):
			if twoDimentWorkedList[y][x] == '0':
				for n in range(1, 10):
					if possible(y, x, str(n)):
						twoDimentWorkedList[y][x] = str(n)
						solve()
						twoDimentWorkedList[y][x] = '0'
				return
	T = copy.deepcopy(twoDimentWorkedList)


def twoDimentionalListToString(newList):
	resultString = ''
	for i in range(len(newList)):
		for j in range(len(newList[i])):
			resultString += str(newList[i][j])
	return resultString

def stringToList(string):
	resultList = []
	for i in range(len(string)):
		if(string[i].isdigit()):
			resultList.append(string[i])
	return resultList




@app.route('/start')
def hello_world():
    return render_template('start.html')


@app.route('/final', methods=['POST'])
def get_message():
	global T, twoDimentWorkedList
	textAreaValue = request.form['my_text_area'].replace(' ', '0')
	workedList = stringToList(textAreaValue)
	twoDimentWorkedList = toTwoDimentionalList(workedList)
	solve()
	resultTextAreaValue = twoDimentionalListToString(T)

	return render_template('final.html',textAreaValue=resultTextAreaValue)


@app.route('/start',methods=['POST'])
def return_to_start():
	return render_template('start.html')

