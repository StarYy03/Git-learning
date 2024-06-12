import requests
import json
import time
import concurrent.futures

url = "http://10.163.171.23:8032/creativity/api/internal/video/paas/poster/draw"

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
          "rotate": 359
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
          "rotate": 359
        },
        "alignment": "justify",
        "fontName": "Source Han Serif CN",
        "fontSize": 40,
        "fontColor": "00000",
        "fontAlpha": 100,
        "bold": False,
        "italic": False,
        "underline": False,
        "lineSpace": 3,
        "wordSpace": 63,
        "vertical": False,
        "shadowConfig": [
          {
            "color": "rgba(0, 0, 0, .5)",
            "hidden": False,
            "offsetAngle": -180,
            "offset": 1,
            "blur": 0
          }
        ],
        "strokeConfig": [
          {
            "color": "#000",
            "width": 0,
            "hidden": False
          }
        ]
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
  'X-dev-origin-user-id': 'test',
  'X-dev-user-account-type': 'passport',
  'Content-Type': 'application/json'
}


def send_request():
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)



with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
  for i in range(7):
    executor.submit(send_request)

