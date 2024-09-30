import ripple_noise as rpn


if __name__ == '__main__':
    # Configure the noise with a Ripple_Noise object.
    # Generate one or more images from a given configuration using the generate_image method.
    noise1 = rpn.Ripple_Noise(size=500, density=10, scale=(0.5, 0.5), strength=1.5, smoothness=3)
    noise1.generate_image('examples/img_1')

    noise_2 = rpn.Ripple_Noise(size=300, density=3)
    noise_2.generate_image('examples/img_2')
    noise_2.generate_image('examples/img_3')

    noise_3 = rpn.Ripple_Noise(300, 8, (0.1, 0.5), 3, 4)
    noise_3.generate_image('examples/img_4')

    noise_4 = rpn.Ripple_Noise(size=500, density=15, scale=(0.3, 0.3))
    noise_4.generate_image('examples/img_5')

    noise_5 = rpn.Ripple_Noise(size=1000, density=2, scale=(0.03, 0.03), strength=1)
    noise_5.generate_image('examples/img_6')
