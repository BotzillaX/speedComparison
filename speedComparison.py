from time import time



def getTime(func, executionRepeat):
    result = 0.0
    for i in range(executionRepeat):
        start_zeit = time()
        func()
        end_zeit = time()
        result += end_zeit - start_zeit
    result = result/executionRepeat
    print(f"Ausführungszeit ohne Library: {result} Sekunden")















if __name__ == "__main__":
    getTime() #input the function followed by an integer to calculate the average speed