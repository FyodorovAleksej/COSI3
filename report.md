

```python
from hopfild import neyron_layer_builder as nlb
from hop_parser import imageParser as imp

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
```

# Д train shape
<img src="./learnShape/D.png" alt="drawing" width="50" height="50"/>
# Н train shape
<img src="./learnShape/H.png" alt="drawing" width="50" height="50"/>
# Х train shape
<img src="./learnShape/X.png" alt="drawing" width="50" height="50"/>


```python
shapes = []
for fileName in learnShapesFiles:
    shape = imp.parse_image_to_shape(fileName)
    if len(shape) == SIZE ** 2:
        print("FIND SHAPE = \"" + fileName + "\"")
        shapes.append(shape)
    else:
        print("FILE IS NOT SHAPE = \"" + fileName + "\"")
```

    FIND SHAPE = "./learnShape/D.png"
    FIND SHAPE = "./learnShape/H.png"
    FIND SHAPE = "./learnShape/X.png"
    


```python
builder = nlb.NeyronLayerBuilder(SIZE ** 2)
for shape in shapes:
    builder.teach(shape)
        
layer = builder.build()
```

# Д test shape
## Д 0% noise test shape
<img src="./testShape/D0.png" alt="drawing" width="50" height="50"/>
## Д 10% noise test shape
<img src="./testShape/D10.png" alt="drawing" width="50" height="50"/>
## Д 20% noise test shape
<img src="./testShape/D20.png" alt="drawing" width="50" height="50"/>
## Д 30% noise test shape
<img src="./testShape/D30.png" alt="drawing" width="50" height="50"/>
## Д 35% noise test shape
<img src="./testShape/D35.png" alt="drawing" width="50" height="50"/>
## Д 40% noise test shape
<img src="./testShape/D40.png" alt="drawing" width="50" height="50"/>
## Д 45% noise test shape
<img src="./testShape/D45.png" alt="drawing" width="50" height="50"/>
## Д 50% noise test shape
<img src="./testShape/D50.png" alt="drawing" width="50" height="50"/>
## Д 60% noise test shape
<img src="./testShape/D60.png" alt="drawing" width="50" height="50"/>
## Д 70% noise test shape
<img src="./testShape/D70.png" alt="drawing" width="50" height="50"/>
## Д 80% noise test shape
<img src="./testShape/D80.png" alt="drawing" width="50" height="50"/>
## Д 90% noise test shape
<img src="./testShape/D90.png" alt="drawing" width="50" height="50"/>
## Д 100% noise test shape
<img src="./testShape/D100.png" alt="drawing" width="50" height="50"/>


# Н test shape
## Н 0% noise test shape
<img src="./testShape/H0.png" alt="drawing" width="50" height="50"/>
## Н 10% noise test shape
<img src="./testShape/H10.png" alt="drawing" width="50" height="50"/>
## Н 20% noise test shape
<img src="./testShape/H20.png" alt="drawing" width="50" height="50"/>
## Н 30% noise test shape
<img src="./testShape/H30.png" alt="drawing" width="50" height="50"/>
## Н 35% noise test shape
<img src="./testShape/H35.png" alt="drawing" width="50" height="50"/>
## Н 40% noise test shape
<img src="./testShape/H40.png" alt="drawing" width="50" height="50"/>
## Н 45% noise test shape
<img src="./testShape/H45.png" alt="drawing" width="50" height="50"/>
## Н 50% noise test shape
<img src="./testShape/H50.png" alt="drawing" width="50" height="50"/>
## Н 60% noise test shape
<img src="./testShape/H60.png" alt="drawing" width="50" height="50"/>
## Н 70% noise test shape
<img src="./testShape/H70.png" alt="drawing" width="50" height="50"/>
## Н 80% noise test shape
<img src="./testShape/H80.png" alt="drawing" width="50" height="50"/>
## Н 90% noise test shape
<img src="./testShape/H90.png" alt="drawing" width="50" height="50"/>
## Н 100% noise test shape
<img src="./testShape/H100.png" alt="drawing" width="50" height="50"/>


# Х test shape
## Х 0% noise test shape
<img src="./testShape/X0.png" alt="drawing" width="50" height="50"/>
## Х 10% noise test shape
<img src="./testShape/X10.png" alt="drawing" width="50" height="50"/>
## Х 20% noise test shape
<img src="./testShape/X20.png" alt="drawing" width="50" height="50"/>
## Х 30% noise test shape
<img src="./testShape/X30.png" alt="drawing" width="50" height="50"/>
## Х 35% noise test shape
<img src="./testShape/X35.png" alt="drawing" width="50" height="50"/>
## Х 40% noise test shape
<img src="./testShape/X40.png" alt="drawing" width="50" height="50"/>
## Х 45% noise test shape
<img src="./testShape/X45.png" alt="drawing" width="50" height="50"/>
## Х 50% noise test shape
<img src="./testShape/X50.png" alt="drawing" width="50" height="50"/>
## Х 60% noise test shape
<img src="./testShape/X60.png" alt="drawing" width="50" height="50"/>
## Х 70% noise test shape
<img src="./testShape/X70.png" alt="drawing" width="50" height="50"/>
## Х 80% noise test shape
<img src="./testShape/X80.png" alt="drawing" width="50" height="50"/>
## Х 90% noise test shape
<img src="./testShape/X90.png" alt="drawing" width="50" height="50"/>
## Х 100% noise test shape
<img src="./testShape/X100.png" alt="drawing" width="50" height="50"/>


```python
for testFile in testShapesFiles:    
    result = layer.test_shape(imp.parse_image_to_shape(testFile))
    out = "result/" + testFile.rsplit(".")[1].split("/")[-1] + "Res.png"
    imp.from_shape_to_image(result, out, SIZE)
```

# Д results
## Д 0% noise   
<input type="checkbox" enabled checked> valid </input>
<img src="result/D0Res.png" alt="drawing" width="50" height="50"/>
## Д 10% noise
<input type="checkbox" enabled checked> valid </input>
<img src="result/D10Res.png" alt="drawing" width="50" height="50"/>
## Д 20% noise
<input type="checkbox" enabled checked> valid </input>
<img src="result/D20Res.png" alt="drawing" width="50" height="50"/>
## Д 30% noise
<input type="checkbox" enabled> valid </input>
<img src="result/D30Res.png" alt="drawing" width="50" height="50"/>
## Д 35% noise
<input type="checkbox" enabled> valid </input>
<img src="result/D35Res.png" alt="drawing" width="50" height="50"/>
## Д 40% noise
<input type="checkbox" enabled> valid </input>
<img src="result/D40Res.png" alt="drawing" width="50" height="50"/>
## Д 45% noise
<input type="checkbox" enabled> valid </input>
<img src="result/D45Res.png" alt="drawing" width="50" height="50"/>
## Д 50% noise
<input type="checkbox" enabled> valid </input>
<img src="result/D50Res.png" alt="drawing" width="50" height="50"/>
## Д 60% noise
<input type="checkbox" enabled> valid </input>
<img src="result/D60Res.png" alt="drawing" width="50" height="50"/>
## Д 70% noise
<input type="checkbox" enabled> valid </input>
<img src="result/D70Res.png" alt="drawing" width="50" height="50"/>
## Д 80% noise
<input type="checkbox" enabled> valid </input>
<img src="result/D80Res.png" alt="drawing" width="50" height="50"/>
## Д 90% noise
<input type="checkbox" enabled> valid </input>
<img src="result/D90Res.png" alt="drawing" width="50" height="50"/>
## Д 100% noise
<input type="checkbox" enabled> valid </input>
<img src="result/D100Res.png" alt="drawing" width="50" height="50"/>

# Н results
## Н 0% noise
<input type="checkbox" enabled checked> valid </input>
<img src="result/H0Res.png" alt="drawing" width="50" height="50"/>
## Н 10% noise
<input type="checkbox" enabled checked> valid </input>
<img src="result/H10Res.png" alt="drawing" width="50" height="50"/>
## Н 20% noise
<input type="checkbox" enabled checked> valid </input>
<img src="result/H20Res.png" alt="drawing" width="50" height="50"/>
## Н 30% noise
<input type="checkbox" enabled> valid </input>
<img src="result/H30Res.png" alt="drawing" width="50" height="50"/>
## Н 35% noise
<input type="checkbox" enabled> valid </input>
<img src="result/H35Res.png" alt="drawing" width="50" height="50"/>
## Н 40% noise
<input type="checkbox" enabled> valid </input>
<img src="result/H40Res.png" alt="drawing" width="50" height="50"/>
## Н 45% noise
<input type="checkbox" enabled> valid </input>
<img src="result/H45Res.png" alt="drawing" width="50" height="50"/>
## Н 50% noise
<input type="checkbox" enabled> valid </input>
<img src="result/H50Res.png" alt="drawing" width="50" height="50"/>
## Н 60% noise
<input type="checkbox" enabled> valid </input>
<img src="result/H60Res.png" alt="drawing" width="50" height="50"/>
## Н 70% noise
<input type="checkbox" enabled> valid </input>
<img src="result/H70Res.png" alt="drawing" width="50" height="50"/>
## Н 80% noise
<input type="checkbox" enabled> valid </input>
<img src="result/H80Res.png" alt="drawing" width="50" height="50"/>
## Н 90% noise
<input type="checkbox" enabled> valid </input>
<img src="result/H90Res.png" alt="drawing" width="50" height="50"/>
## Н 100% noise
<input type="checkbox" enabled> valid </input>
<img src="result/H100Res.png" alt="drawing" width="50" height="50"/>

# Х results
## Х 0% noise
<input type="checkbox" enabled checked> valid </input>
<img src="result/X0Res.png" alt="drawing" width="50" height="50"/>
## Х 10% noise
<input type="checkbox" enabled checked> valid </input>
<img src="result/X10Res.png" alt="drawing" width="50" height="50"/>
## Х 20% noise
<input type="checkbox" enabled checked> valid </input>
<img src="result/X20Res.png" alt="drawing" width="50" height="50"/>
## Х 30% noise
<input type="checkbox" enabled checked> valid </input>
<img src="result/X30Res.png" alt="drawing" width="50" height="50"/>
## Х 35% noise
<input type="checkbox" enabled checked> valid </input>
<img src="result/X35Res.png" alt="drawing" width="50" height="50"/>
## Х 40% noise
<input type="checkbox" enabled> valid </input>
<img src="result/X40Res.png" alt="drawing" width="50" height="50"/>
## Х 45% noise
<input type="checkbox" enabled> valid </input>
<img src="result/X45Res.png" alt="drawing" width="50" height="50"/>
## Х 50% noise
<input type="checkbox" enabled> valid </input>
<img src="result/X50Res.png" alt="drawing" width="50" height="50"/>
## Х 60% noise
<input type="checkbox" enabled> valid </input>
<img src="result/X60Res.png" alt="drawing" width="50" height="50"/>
## Х 70% noise
<input type="checkbox" enabled> valid </input>
<img src="result/X70Res.png" alt="drawing" width="50" height="50"/>
## Х 80% noise
<input type="checkbox" enabled> valid </input>
<img src="result/X80Res.png" alt="drawing" width="50" height="50"/>
## Х 90% noise
<input type="checkbox" enabled> valid </input>
<img src="result/X90Res.png" alt="drawing" width="50" height="50"/>
## Х 100% noise
<input type="checkbox" enabled> valid </input>
<img src="result/X100Res.png" alt="drawing" width="50" height="50"/>

