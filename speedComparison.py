from time import time

def getTime(func, executionRepeat):
    result = 0.0
    for i in range(executionRepeat):
        startTime = time()
        func()
        endTime = time()
        result += endTime - startTime
    result /= executionRepeat
    print("Execution took: {:.10f} seconds".format(result))
















if __name__ == "__main__":
    getTime() #input the function followed by an integer to calculate the average speed