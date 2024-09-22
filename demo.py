import ripple_noise as rpn

if __name__ == '__main__':
    img_1 = rpn.Ripple_Noise('img_1', 500, 3)
    img_1.save_image()
    print('Image 1 generated.')

    img_2 = rpn.Ripple_Noise('img_2', 500, 8, 0.2)
    img_2.save_image()
    print('Image 2 generated.')

    img_3 = rpn.Ripple_Noise('img_3', 500, 2, 0.03, 1)
    img_3.save_image()
    print('Image 3 generated.')