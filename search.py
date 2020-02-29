import sys

import requests
import pygame

from params_finder import find_params

# Я сделал показ картинки через pygame, ибо встроенный просмотрщик очень кривой.
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]

params, sizex, sizey = find_params(toponym)
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=params)

with open("toponym_image", "wb") as file:
    file.write(response.content)
pygame.init()
screen = pygame.display.set_mode((sizex, sizey))
screen.blit(pygame.image.load("toponym_image"), (0, 0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
