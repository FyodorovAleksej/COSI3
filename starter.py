from hopfild import neyron_layer_builder as nlb
from hop_parser import imageParser as imp

if __name__ == "__main__":
    SIZE = 10

    learnShapesFiles = [
        "./learnShape/D.png",
        "./learnShape/H.png",
        "./learnShape/X.png"
    ]

    testShapesFiles = [
        "./testShape/D0.png",
        "./testShape/D10.png",
        "./testShape/D20.png",
        "./testShape/D30.png",
        "./testShape/D35.png",
        "./testShape/D40.png",
        "./testShape/D45.png",
        "./testShape/D50.png",
        "./testShape/D60.png",
        "./testShape/D70.png",
        "./testShape/D80.png",
        "./testShape/D90.png",
        "./testShape/D100.png",

        "./testShape/H0.png",
        "./testShape/H10.png",
        "./testShape/H20.png",
        "./testShape/H30.png",
        "./testShape/H35.png",
        "./testShape/H40.png",
        "./testShape/H45.png",
        "./testShape/H50.png",
        "./testShape/H60.png",
        "./testShape/H70.png",
        "./testShape/H80.png",
        "./testShape/H90.png",
        "./testShape/H100.png",

        "./testShape/X0.png",
        "./testShape/X10.png",
        "./testShape/X20.png",
        "./testShape/X30.png",
        "./testShape/X35.png",
        "./testShape/X40.png",
        "./testShape/X45.png",
        "./testShape/X50.png",
        "./testShape/X60.png",
        "./testShape/X70.png",
        "./testShape/X80.png",
        "./testShape/X90.png",
        "./testShape/X100.png"
    ]

    shapes = []
    for fileName in learnShapesFiles:
        shape = imp.parse_image_to_shape(fileName)
        if len(shape) == SIZE ** 2:
            print("FIND SHAPE = \"" + fileName + "\"")
            shapes.append(shape)
        else:
            print("FILE IS NOT SHAPE = \"" + fileName + "\"")
    builder = nlb.NeyronLayerBuilder(SIZE ** 2)
    print(len(shapes))
    for shape in shapes:
        builder.teach(shape)

    layer = builder.build()

    for testFile in testShapesFiles:
        print(testFile)
        result = layer.test_shape(imp.parse_image_to_shape(testFile))
        out = "result/" + testFile.rsplit(".")[1].split("/")[-1] + "Res.png"
        imp.from_shape_to_image(result, out, SIZE)
