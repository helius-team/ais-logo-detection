from pycocotools.coco import COCO

"""/home/andrii/edu/helius/ais-logo-detection/instances_train2017.json"""
# dataDir='..'
# dataType='train2017'
# annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile = "instances_train2017.json"
coco = COCO(annFile)
catIds = coco.getCatIds(catNms=['person','car']);
imgIds = coco.getImgIds(catIds=catIds)
img = coco.loadImgs(imgIds)

for i, im in enumerate(img):
    # prinimg.keys()
    if i % 10 == 0:
        try:
            urllib.request.urlretrieve(im['flickr_url'], 'load/' + im['flickr_url'].split("/")[-1])
        except:
            urllib.request.urlretrieve(im['coco_url'], 'load/' + im['coco_url'].split("/")[-1])
