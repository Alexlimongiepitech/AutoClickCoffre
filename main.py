#!/usr/bin/python
import screen_search
import cv2
import random
import pyautogui
import time
import tkinter
import sys
import asyncio
import threading

class Coffre_twitch():
    def __init__(self):
        self.imagePath = "coffre_twitch.png"
        self.searchClass = screen_search.Search(self.imagePath)
        self.position = list
        self.countFind = int = 0
        self.howManyYouWantToFind = int
        self.howManyDontFind = int = 0
        self.img = cv2.imread(self.imagePath)
        self.heightOfImage, self.widthOfImage, self.channelsOfImage = self.img.shape
        self.breakWhile = True

    def _asyncio_thread(self, async_loop):
        # async_loop.run_forever(self.run())
        async_loop.run_until_complete(self.run())

    def _asyncio_thread_stop(self, async_loop):
        async_loop.stop()
        async_loop.close()

    def setHowManyYouWantToFind(self, howManyYouWantToFind_):
        try:
            self.howManyYouWantToFind = int(howManyYouWantToFind_)
            return True
        except ValueError:
            return False

    def searchImage(self):
        pos = self.searchClass.imagesearch()
        if (pos[0] != -1):
            self.position = pos
            return True
        else:
            return False

    def clickOnImage(self):
        pyautogui.moveTo(self.position[0] + random.randint(self.widthOfImage / 2, (self.widthOfImage / 2) + 10),
                         self.position[1] + random.randint(self.heightOfImage / 2, (self.heightOfImage / 2) + 10))
        pyautogui.click(button="left")

    async def run(self):
        self.howManyDontFind = 0
        self.countFind = 0
        while (self.breakWhile != True):
            # print(self.countFind, self.howManyYouWantToFind)
            if  (self.countFind == self.howManyYouWantToFind):
                return
            timeToSleep = random.randint(60, 75 + self.countFind)
            timeRemeber = 0
            # print(self.breakWhile)
            if (self.searchImage() == True):
                self.countFind = self.countFind + 1
                print("Image found at position : {} {}\t countFind = {} / try left = {}"
                      .format(self.position[0], self.position[1], self.countFind, self.howManyYouWantToFind - self.countFind))
                self.clickOnImage()
                # await asyncio.sleep(random.randint(60, 75 + self.countFind))
                # await time.sleep(random.randint(60, 75 + self.countFind))
                # asyncio.sleep(random.randint(60, 75 + self.countFind))
                # time.sleep(random.randint(60, 75 + self.countFind))
            else:
                self.howManyDontFind = self.howManyDontFind + 1
                print("Image not found, howManyDontFind = {}".format(self.howManyDontFind))
                # await asyncio.sleep(random.randint(30, 45 + self.countFind))
                # await time.sleep(random.randint(30, 45 + self.countFind))
                # asyncio.sleep(random.randint(30, 45 + self.countFind))
                # time.sleep(random.randint(30, 45 + self.countFind))

            while (timeToSleep != timeRemeber):
                if (self.breakWhile == True):
                    return
                timeRemeber = timeRemeber + 1
                time.sleep(1)
                # print("one sec pass")
        return

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Auto Click Coffre")
        self.coffre_twitch = Coffre_twitch()
        self.master = master
        self.pack()
        self.create_widgets()
        self.async_loop = asyncio.get_event_loop()
        self.clock()
        self.myTask = None

    def create_widgets(self):
        # self.labelHello = tkinter.Label(self, text="Auto Click Coffre", font=("Arial Bold", 30))
        # self.labelHello.grid(column=1, row=0)
        countFindTextStatus_var = tkinter.StringVar()
        countFindTextStatus_var.set(str(self.coffre_twitch.countFind))
        howManyDontFindStatus_var = tkinter.StringVar()
        howManyDontFindStatus_var.set(str(self.coffre_twitch.howManyDontFind))
        tryLeft_var = tkinter.StringVar()
        tryLeft_var.set(str(self.coffre_twitch.howManyYouWantToFind - self.coffre_twitch.countFind))
        # self.master.update_idletasks()

        self.labelText = tkinter.Label(self, text="Number : ", font=("Arial Bold", 15))
        self.labelText.grid(sticky=tkinter.W)

        self.entryText = tkinter.Entry(self, width=20)
        self.entryText.grid(column=1, row=0, sticky=tkinter.W)

        self.startButton = tkinter.Button(self, text="Start", font=("Arial Bold", 15), command=self.startFun)
        self.startButton.grid(column=0, row=1)
        self.stopButton = tkinter.Button(self, text="Stop", font=("Arial Bold", 15), command=self.endFun)
        self.stopButton.grid(column=1, row=1)

        self.statusText = tkinter.Label(self, text="Status : ", font=("Arial Bold", 15))
        self.statusText.grid(column=0, row=2, sticky=tkinter.W)
        self.actualStatusText = tkinter.Label(self, text="Stop", font=("Arial Bold", 15))
        self.actualStatusText.grid(column=1, row=2, sticky=tkinter.E)

        self.countFindText = tkinter.Label(self, text="countFind : ", font=("Arial Bold", 15))
        self.countFindText.grid(column=0, row=3, sticky=tkinter.W)
        self.countFindTextStatus = tkinter.Label(self, textvariable=countFindTextStatus_var, font=("Arial Bold", 15))
        self.countFindTextStatus.grid(column=1, row=3, sticky=tkinter.E)

        self.howManyDontFindText = tkinter.Label(self, text="howManyDontFind : ", font=("Arial Bold", 15))
        self.howManyDontFindText.grid(column=0, row=4, sticky=tkinter.W)
        self.howManyDontFindStatusText = tkinter.Label(self, textvariable=howManyDontFindStatus_var, font=("Arial Bold", 15))
        self.howManyDontFindStatusText.grid(column=1, row=4, sticky=tkinter.E)

        self.tryLeftText = tkinter.Label(self, text="Try left : ", font=("Arial Bold", 15))
        self.tryLeftText.grid(column=0, row=5, sticky=tkinter.W)
        self.tryLeftTextStatus = tkinter.Label(self, textvariable=tryLeft_var, font=("Arial Bold", 15))
        self.tryLeftTextStatus.grid(column=1, row=5, sticky=tkinter.E)

        self.errorText = tkinter.Label(self, font=("Arial Bold", 15), fg="red")
        self.errorText.grid()

        # self.hi_there = tkinter.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        # self.quit = tkinter.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")

    def clock(self):
        countFindTextStatus_var = tkinter.StringVar()
        countFindTextStatus_var.set(str(self.coffre_twitch.countFind))
        howManyDontFindStatus_var = tkinter.StringVar()
        howManyDontFindStatus_var.set(str(self.coffre_twitch.howManyDontFind))
        tryLeft_var = tkinter.StringVar()
        tryLeft_var.set(str(self.coffre_twitch.howManyYouWantToFind - self.coffre_twitch.countFind))

        self.countFindTextStatus.config(textvariable=countFindTextStatus_var)
        self.howManyDontFindStatusText.config(textvariable=howManyDontFindStatus_var)
        self.tryLeftTextStatus.config(textvariable=tryLeft_var)
        self.master.after(1000, self.clock)

    # def startFun(self):
    #     if (self.coffre_twitch.setHowManyYouWantToFind(self.entryText.get()) == True):
    #         self.errorText["text"] = ""
    #         self.actualStatusText["text"] = "Work"
    #         print("succefully set")
    #         asyncio.run(self.coffre_twitch.run())
    #         # self.coffre_twitch.main()
    #     else:
    #         self.errorText["text"] = "Enter int"
    #         print("Fail set")
    #     # print(self.howManyYouWantToFind.get())

    def startFun(self):
        if (self.coffre_twitch.breakWhile == False):
            self.errorText["text"] = "Already in work"
            print("Already in work")
            return
        
        if (self.coffre_twitch.setHowManyYouWantToFind(self.entryText.get()) == True):
            self.errorText["text"] = ""
            self.actualStatusText["text"] = "Work"
            self.coffre_twitch.breakWhile = False
            print("succefully set")
            self.myTask = threading.Thread(target=self.coffre_twitch._asyncio_thread, args=(self.async_loop,))
            self.myTask.start()
            # asyncio.run(self.coffre_twitch.run())
            # self.coffre_twitch.main()
            return
        else:
            self.errorText["text"] = "Enter int"
            print("Fail set")
            return

    def endFun(self):
        self.errorText["text"] = ""
        self.actualStatusText["text"] = "Stop"
        # self.myTask._stop()
        # self.myTask.daemon = False
        # self.myTask._delete()
        self.coffre_twitch.breakWhile = True
        # self.coffre_twitch._asyncio_thread_stop(self.async_loop)
        # self.myTask.join()
        # del self.myTask
        # sys.exit()
        # raise KeyboardInterrupt

if __name__ == "__main__":
    # if (len(sys.argv) == 2):
    #     coffre_twitch(int(sys.argv[1])).main()
    # else:
    #     print("{} howManyYouWantToFind".format(sys.argv[0]))

    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()
    # app.update_idletasks()