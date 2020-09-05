from collections import defaultdict


class Boggle:
    M = 3
    N = 3

    def __init__(self):
        self.wordList = ["GEEKS", "FOR", "QUIZ", "GUQ", "EE"]

    def isWord(self, word):
        if(word in self.wordList):
            return True
        return False

    def findWords(self, boggle):
        isVisited = [ [False for j in range(Boggle.N)] for i in range(Boggle.M)]
        word = ""
        outputWordDict = defaultdict(bool)
        for i in range(Boggle.M):
            for j in range(Boggle.N):
                self.findWordsRecurse(boggle, isVisited, i, j, word, outputWordDict)

    def findWordsRecurse(self, boggle, isVisited, i, j, word, outputWordDict):
        isVisited[i][j] = True
        word += boggle[i][j]
        outputWordDict[word] 
        if(outputWordDict[word] == False and self.isWord(word)):
            outputWordDict[word] = True
            print(word)

        row = i - 1
        while(row <= i + 1 and row < Boggle.M):
            col = j - 1
            while(col <= j + 1 and col < Boggle.N):
                if(row >= 0 and col >= 0 and isVisited[row][col] == False):
                    self.findWordsRecurse(boggle, isVisited, row, col, word, outputWordDict)
                col += 1
            row += 1
        
        word = "" + word[len(word) - 1]
        isVisited[i][j] = False



boggle = [['G', 'I', 'Z'],
          ['U', 'E', 'K'],
          ['Q', 'S', 'E']]

Boggle().findWords(boggle)