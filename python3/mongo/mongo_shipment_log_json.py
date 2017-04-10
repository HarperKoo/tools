#!/usr/bin/python3
import json
from pprint import pprint

jstr = {
  "_id": {
    "$oid": "58af8f6681688630d09fe907"
  },
  "shipment": {
    "$ref": "shipment",
    "$id": {
      "$oid": "58af8e5881688630d09fd6f7"
    }
  },
  "container": {
    "barcode": "0100041486",
    "code": "인천82아9914",
    "typeCode": "T17",
    "typeName": "11t",
    "typeGroup": "LINEHAULTRUCK"
  },
  "containerUsage": {
    "id": {
      "$numberLong": 11090
    },
    "container": {
      "barcode": "0100041486",
      "code": "인천82아9914",
      "typeCode": "T17",
      "typeName": "11t",
      "typeGroup": "LINEHAULTRUCK"
    },
    "originWorkplace": {
      "id": 81,
      "code": "5",
      "name": "인천4HUB",
      "type": "HUB"
    },
    "destinationWorkplace": {
      "id": 85,
      "code": "8",
      "name": "칠곡HUB",
      "type": "HUB"
    },
    "totalShipmentQuantity": 533,
    "totalShipmentWeight": 838380,
    "totalShipmentVolume": {
      "$numberLong": "9146143800"
    }
  },
  "invoiceNumber": "10171451773755",
  "orderNumber": {
    "$numberLong": "8000004926554"
  },
  "worker": {
    "id": 49,
    "username": "in0032",
    "fullName": "in0032 (안병도)"
  },
  "status": "CENTER_LOADED",
  "workplace": {
    "id": 81,
    "code": "5",
    "name": "인천4HUB",
    "type": "HUB"
  },
  "targetWorkplace": {
    "id": 85,
    "code": "8",
    "name": "칠곡HUB",
    "type": "HUB"
  },
  "happenedAt": {
    "$date": "2017-02-24T01:40:19Z"
  },
  "createdBy": "in0032",
  "createdAt": {
    "$date": "2017-02-24T01:41:58.184Z"
  },
  "updatedBy": "in0032",
  "updatedAt": {
    "$date": "2017-02-24T01:41:58.184Z"
  }
}

data_str = json.dumps(jstr)
data = json.loads(data_str)
pprint(data)