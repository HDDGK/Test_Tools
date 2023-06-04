import PIL
from PIL import Image
import numpy as np

def Draw_HandleDraw(picture_address):
    a=np.asarray(Image.open(picture_address).convert('L')).astype('float')

    depth=20
    grad=np.gradient(a)
    grad_x,grad_y=grad
    grad_x=grad_x*depth/100
    grad_y=grad_y*depth/100
    A=np.sqrt(grad_x**2+grad_y**2+1.)
    uni_x=grad_x/A
    uni_y=grad_y/A
    uni_z=1./A

    vec_el=np.pi/2.2
    vec_az=np.pi/4.
    dx=np.cos(vec_el)*np.cos(vec_az)
    dy=np.cos(vec_el)*np.sin(vec_az)
    dz=np.sin(vec_el)

    b=255*(dx*uni_x+dy*uni_y+dz*uni_z)
    b=b.clip(0.255)
    im=Image.fromarray(b.astype('uint8'))
    im.save(r"C:\Users\HK145-TP\Desktop\HandleDraw.png")
    pass

def Draw(picture_address):
    # im = np.array(Image.open(picture_address).convert('L'))
    im = np.array(Image.open(picture_address))
    im2 = Image.fromarray(im.astype('uint8'))
    # im2.save(r"C:\Users\HK145-TP\Desktop\125.png")
    GM= 255 * (im / 255) ** 2
    im2 = Image.fromarray(GM.astype('uint8'))
    im2.save(r"C:\Users\HK145-TP\Desktop\Heavy.png")


def main():
    picture_list=[r"C:\Users\HK145-TP\Desktop\老师.jpg",
                  r"C:\Users\HK145-TP\Desktop\123.png",
                  r"C:\Users\HK145-TP\Desktop\111.png",
                  r"C:\Users\HK145-TP\Desktop\电风扇.jpg",

                  ]
    # Draw(picture_list[0])
    Draw_HandleDraw(picture_list[3])


if __name__ == '__main__':
    main()