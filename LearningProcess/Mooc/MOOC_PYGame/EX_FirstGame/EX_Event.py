import pygame,sys

def event_post():
    pygame.init()
    screen=pygame.display.set_mode((600,400))
    pygame.display.set_caption("Pygame游戏")
    fps=1
    flock=pygame.time.Clock()
    num=1
    while True:
        Uevent=pygame.event.Event(pygame.KEYDOWN,{"unicode":123,"key":pygame.K_SPACE,'mod':pygame.KMOD_ALT})
        pygame.event.post(Uevent)
        num=num+1
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.unicode=="":
                    print("[KEYDOWN{}]".format(num),"#",event.key,event.mod)
                else:
                    print("[KEYDOWN{}]".format(num), event.unicode, event.key, event.mod)
        pygame.display.update()
        flock.tick(fps)
if __name__ == '__main__':
    event_post()