import requests
import json
import concurrent.futures
from datetime import datetime
url = "https://aip.baidubce.com/rpc/2.0/brain/internal/video/paas/poster/draw?access_token=24.1e52ef927c7c95891cff0c656f014c87.2592000.1720254008.282335-79185518"

payload = json.dumps({
  "metaData": {
    "width": 1280,
    "height": 1920,
    "format": "JPG",
    "fileName": "AI海报_20240528_1",
    "order": 0
  },
  "content": [
    {
      "type": "IMAGE",
      "layer": 0,
      "imageInfo": {
        "mediaSource": {
          "url": "https://creative-static.cdn.bcebos.com/public/F01DAF27445D4DAD82BF8DE8A57CF440.png"
        },
        "originWidth": 720,
        "originHeight": 1280,
        "location": {
          "width": 720,
          "height": 1280,
          "x": 7,
          "y": 0,
          "crop": {
            "offsetX": 0,
            "offsetY": 0,
            "croppedWidth": 720,
            "croppedHeight": 1280
          },
          "rotate": 0
        },
        "imageAlpha": 100
      }
    },
    {
      "type": "TEXT",
      "layer": 1,
      "textInfo": {
        "text": "点击编辑文字",
        "location": {
          "width": 400,
          "height": 99,
          "x": 159,
          "y": 175,
          "rotate": 30
        },
        "alignment": "left",
        "fontName": "Source Han Serif CN",
        "fontSize": 66,
        "fontColor": "00000",
        "fontAlpha": 100,
        "bold": False,
        "italic": False,
        "underline": False,
        "lineSpace": 1.5,
        "wordSpace": 0,
        "vertical": False
      }
    },
    {
      "type": "IMAGE",
      "layer": 2,
      "imageInfo": {
        "mediaSource": {
          "url": "https://creative-static.cdn.bcebos.com/public/F01DAF27445D4DAD82BF8DE8A57CF440.png"
        },
        "originWidth": 351,
        "originHeight": 608,
        "location": {
          "width": 276,
          "height": 479,
          "x": 221,
          "y": 354,
          "crop": {
            "offsetX": 0,
            "offsetY": 0,
            "croppedWidth": 276.6737291412379,
            "croppedHeight": 479.2524994811191
          },
          "rotate": 0
        }
      }
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}


def send_request():
  start_time = datetime.now()
  response = requests.request("POST", url, headers = headers, data = payload)
  end_time = datetime.now() - start_time
  print(f"Request time: {end_time}")
  print(response.text)

send_request()

# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#   for i in range(5):
#     executor.submit(send_request)
