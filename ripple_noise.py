import random
import math
from PIL import Image


'''
Class for generating noise texture images
'''
class Ripple_Noise:
    IMG_EXT = '.png'


    '''
    Constructor

    name: name of noise image
    size: size of image
    density: density of noise pattern
    scale: scale of noise pattern
    strength: strength of noise pattern
    smoothness: smoothness of noise pattern
    '''
    def __init__(self, size: int, density: int, scale=0.1, strength=0.75, smoothness=2) -> None:
        self.__validate_parameters(size, density, smoothness)

        self.size = size
        self.density = density

        self.delta = self.size // self.density
        self.scale = scale * self.delta
        self.strength = strength * self.delta
        self.smoothness = smoothness


    '''
    Validate constructor parameters
    '''
    def __validate_parameters(self, size: int, density: int, smoothness: int) -> None:
        if size < 1:
            Exception('Size must be positive.')

        if density < 1 or size < density:
            Exception('Density must be greater than 0 and less than size.')

        if smoothness < 0 or density <= smoothness:
            Exception('Smoothness must be nonnegative and less than density.')


    '''
    Create image to hold noise pattern
    '''
    def __init_image(self) -> None:
        self.image = Image.new('RGB', (self.size, self.size))
        self.pixels = self.image.load()
    
    
    '''
    Designate seeds within image space

    Seeds are the points from which "ripples" emanate
    '''
    def __seed_image(self) -> None:
        self.seeds = []

        for i in range(self.density):
            row = i * self.delta
            self.seeds.append([])

            for j in range(self.density):
                col = j * self.delta
                seed = (random.randint(row, row + self.delta), random.randint(col, col + self.delta))
                self.seeds[i].append(seed)


    '''
    Determine lightness of pixel from distance to seed
    '''
    def __value_function(self, dist: int) -> int:
        value = 255 * math.cos(math.pi * dist / self.scale)
        value *= math.exp(-((dist / self.strength) ** 2))
        return math.floor(value)
    

    '''
    Return nearest seeds to pixel
    
    Note: higher smoothness values cause more seeds to be considered per pixel.
    '''
    def __nearest_seeds(self, x: int, y: int) -> list:
        row = x // self.delta
        col = y // self.delta

        nearest_seeds = []
        for i in range(row - self.smoothness, row + self.smoothness + 1):
            if 0 <= i < self.density:
                for j in range(col - self.smoothness, col + self.smoothness + 1):
                    if 0 <= j < self.density:
                        nearest_seeds.append(self.seeds[i][j])

        return nearest_seeds
    

    '''
    Set lightness of single pixel
    '''
    def __set_pixel_value(self, x: int, y: int) -> None:
        value = 0 
        nearest_seeds = self.__nearest_seeds(x, y)

        for seed in nearest_seeds:
            dist = math.sqrt(((x - seed[0]) ** 2) + ((y - seed[1]) ** 2))
            value += self.__value_function(dist)
        
        value = min(value, 255)
        self.pixels[x, y] = (value, value, value)


    '''
    Fill image with noise texture
    '''
    def __fill_image(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                self.__set_pixel_value(i, j)


    '''
    Generate and save noise image
    '''
    def generate_image(self, name: str) -> None:
        self.__init_image()
        self.__seed_image()
        self.__fill_image()
        self.image.save(name + Ripple_Noise.IMG_EXT)
