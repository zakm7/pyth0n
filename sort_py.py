'''
Python Sorting Visualizer using Tk module.
This has Bubble, Selection and Insertion Sort implemented.
Mohamed Zakim [21/9/22]
'''

import tkinter as tk
import random

# global iterator
worker = None 

#swap two bars
def swap(first_pos, second_pos):
    bar11, _, bar12, _ = canvas.coords(first_pos)
    bar21, _, bar22, _ = canvas.coords(second_pos)
    canvas.move(first_pos, bar21-bar11, 0)
    canvas.move(second_pos, bar12-bar22, 0)


#insertion Sort
def _insertion_sort():
    #barList will have bars from 1 to 60
    global barList
    #lenghtList will have lenghts of bars generated randomly
    global lengthList

    window.title("[Insertion Sort] Worst: O(N^2), Best: O(N)")

    #insertion sort logic
    for i in range(len(lengthList)):
        cursor = lengthList[i]
        cursorBar = barList[i]
        pos = i

        while pos > 0 and lengthList[pos - 1] > cursor:
            lengthList[pos] = lengthList[pos - 1]
            barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
            swap(barList[pos],barList[pos-1])   
            yield                                      
            pos -= 1                                   

        lengthList[pos] = cursor
        barList[pos] = cursorBar
        swap(barList[pos],cursorBar)


#bubble Sort
def _bubble_sort():
    global barList
    global lengthList

    window.title("[Bubble Sort] Worst: O(N^2), Best: O(N)")
    
    #bubble sort logic
    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if(lengthList[j] > lengthList[j + 1]):
                lengthList[j] , lengthList[j + 1] = lengthList[j + 1] , lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1] , barList[j]
                swap(barList[j + 1] , barList[j])
                yield      
           

#selection Sort            
def _selection_sort():
    global barList    
    global lengthList

    window.title("[Bubble Sort] Worst: O(N^2), Best: O(N^2)")

    #selection sort logic
    for i in range(len(lengthList)):
        min = i
        for j in range(i + 1 ,len(lengthList)):
            if(lengthList[j] < lengthList[min]):
                min = j
        lengthList[min], lengthList[i] = lengthList[i] ,lengthList[min]
        barList[min] , barList[i] = barList[i] , barList[min]
        swap(barList[min] , barList[i])        
        yield


#animate function
def animate():      
    global worker
    if worker is not None:
        try:
            next(worker)
            window.after(10, animate)    
        except StopIteration:            
            worker = None
        finally:
            window.after_cancel(animate) 


#functions that are triggered on button event
def insertion_sort():    
    global worker
    worker = _insertion_sort()
    animate()

def selection_sort():     
    global worker
    worker = _selection_sort()
    animate()

def bubble_sort():     
    global worker
    worker = _bubble_sort()
    animate()    


#generator function for generating rectangular sort values
def generate():
    global barList
    global lengthList
    canvas.delete('all')
    barstart = 7
    barend = 14
    barList = []
    lengthList = []

    #Creating 60 rectangles
    for bar in range(1, 60):

        #to generate bars of random lengths
        randomY = random.randint(1, 360)

        bar = canvas.create_rectangle(barstart, randomY, barend, 365, fill='DarkGrey')

        barList.append(bar)
        barstart += 10
        barend += 10

    #getting length of the bar and appending into length list
    for bar in barList:

        # returns  the cordinates of each bar from 1 - 60
        bar = canvas.coords(bar)
        
        # calculate lenght of each rectangle
        length = bar[3] - bar[1]

        lengthList.append(length)

    #colour max bar and min bar as grey for easy visualization
    for i in range(len(lengthList)-1):
        if lengthList[i] == min(lengthList):
            canvas.itemconfig(barList[i], fill='grey29')
        elif lengthList[i] == max(lengthList):
            canvas.itemconfig(barList[i], fill='grey12')



#making a window
window = tk.Tk()
window.title('Python Sorting Visualizer')
window.geometry('600x450')

#making a canvas widget
canvas = tk.Canvas(window, width='600', height='400')
canvas.grid(column=0,row=0, columnspan = 70)
canvas.configure(bg='LightSkyBlue1')

#buttons
bubble = tk.Button(window, text='Bubble Sort', command=bubble_sort)
select = tk.Button(window, text='Selection Sort', command=selection_sort)
insert = tk.Button(window, text='Insertion Sort', command=insertion_sort)
shuf = tk.Button(window, text='Shuffle', command=generate, bg="LightSteelBlue").place(x=510, y=412);

#button positioning
bubble.grid(column=0,row=1)
select.grid(column=1,row=1)
insert.grid(column=2,row=1)

generate()
window.mainloop()




