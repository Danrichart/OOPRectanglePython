from Tkinter import *

class Rectangle(object):
    def __init__(self, width=5, height=3):
        object.__init__(self)
        self.setWidth(width)
        self.setHeight(height)

    def setWidth(self, width):
        self.__width = width

    def getWidth(self):
        return self.__width
    
    width = property(fget = getWidth, fset = setWidth)
    
    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    height = property(fget = getHeight, fset = setHeight)
        
    def getArea(self):
        return self.getWidth() * self.getHeight()

    area = property(fget = getArea)

    def getPerimeter(self):
        return (self.getWidth() * 2) + (self.getHeight() * 2)

    perimeter = property(fget = getPerimeter)

    def getStats(self):
        output = ""
        output +="height:    %d\n" % self.height
        output +="width:     %d\n" % self.width
        output +="area:      %d\n" % self.area
        output +="perimeter: %d\n" % self.perimeter
        return output


app = Tk()
lblWidth = Label(app, text = "Type the Width:")
lblWidth.grid(padx=30, pady=10)
txtWidth = Entry(app)
txtWidth.grid()

lblHeight = Label(app, text = "Type the Height:")
lblHeight.grid()
txtHeight = Entry(app)
txtHeight.grid()

btnCalculate = Button(app, text = "Calculate")
btnCalculate.grid()

lblOutput = Label(app, text = "")
lblOutput.grid(pady=20)

def rectangleCalculate():
    r = Rectangle(int(txtWidth.get()),int(txtHeight.get()))
    lblOutput["text"] = r.getStats()

btnCalculate["command"] = rectangleCalculate

app.mainloop()











