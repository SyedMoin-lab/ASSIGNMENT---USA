from gtts import gTTS
import pygame
import moviepy.editor as mp

text = "Hello! This is a demo of text-to-video conversion with an avatar."
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")

pygame.init()
screen = pygame.display.set_mode((640, 480))

avatar_img = pygame.image.load('avatar.png')
avatar_rect = avatar_img.get_rect(center=(320, 240))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    avatar_rect.x += 1 if avatar_rect.x < 640 else -640
    screen.fill((255, 255, 255))
    screen.blit(avatar_img, avatar_rect)
    pygame.display.flip()

    pygame.time.delay(3000)
    running = False

pygame.quit()

video_clip = mp.ImageClip('avatar.png', duration=5)
audio_clip = mp.AudioFileClip('output.mp3')
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile("text_to_video_demo.mp4", fps=24)
