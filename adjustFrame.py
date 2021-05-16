from tkinter import Toplevel, Label, Scale, Button, HORIZONTAL, RIGHT
import cv2


class AdjustFrame(Toplevel):

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.brightness_value = 0
        self.previous_brightness_value = 0

        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image

        self.brightness_label = Label(self, text="Brightness", fg="#66FF66", font="comicsansms 12 bold")
        self.brightness_scale = Scale(self, from_=0, to_=2, length=250, resolution=0.1,
                                      orient=HORIZONTAL, background="#FFFF31")
        self.r_label = Label(self, text="R", fg="#FF0000", font="comicsansms 12 bold")
        self.r_scale = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL, background="#FF0000")
        self.g_label = Label(self, text="G", fg="#008000", font="comicsansms 12 bold")
        self.g_scale = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL, background="#008000")
        self.b_label = Label(self, text="B", fg="#0000FF", font="comicsansms 12 bold")
        self.b_scale = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL, background="#0000FF")
        self.apply_button = Button(self, text="Apply", font="TimesNewRoman 14", fg="white", bg="#FF007C")
        self.preview_button = Button(self, text="Preview", font="TimesNewRoman 14", fg="white", bg="#FF007C")
        self.cancel_button = Button(self, text="Cancel", font="TimesNewRoman 14", fg="white", bg="#FF007C")

        self.brightness_scale.set(1)

        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.preview_button.bind("<ButtonRelease>", self.show_button_release)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.brightness_label.pack()
        self.brightness_scale.pack()
        self.r_label.pack()
        self.r_scale.pack()
        self.g_label.pack()
        self.g_scale.pack()
        self.b_label.pack()
        self.b_scale.pack()
        self.cancel_button.pack(side=RIGHT, pady=10, padx=5)
        self.preview_button.pack(side=RIGHT, pady=10, padx=5)
        self.apply_button.pack(pady=10, side=RIGHT)

    def apply_button_released(self, event):
        self.master.processed_image = self.processing_image
        self.close()

    def show_button_release(self, event):
        self.processing_image = cv2.convertScaleAbs(self.original_image, alpha=self.brightness_scale.get())
        b, g, r = cv2.split(self.processing_image)

        for b_value in b:
            cv2.add(b_value, self.b_scale.get(), b_value)
        for g_value in g:
            cv2.add(g_value, self.g_scale.get(), g_value)
        for r_value in r:
            cv2.add(r_value, self.r_scale.get(), r_value)

        self.processing_image = cv2.merge((b, g, r))
        self.show_image(self.processing_image)

    def cancel_button_released(self, event):
        self.close()

    def show_image(self, img=None):
        self.master.image_viewer.show_image(img=img)

    def close(self):
        self.show_image()
        self.destroy()
