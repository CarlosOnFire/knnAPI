from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

import json

# Create your views here.

class KnnCore(APIView):

    self.validData

    def __init__(self, data):
        self.setData(data)

    def setData(self, data):
        """
            Thiss Method catches json formatted data and save it in memory
            json string object structure:
                    
                    {
                        "cuartos":int,
                        "area":int,
                        "pisos":int,
                        "tipo":string
                     }

            data -- json string with the values
        """
        #TODO: turn json to model array and save it
        self.validData=data

    def getData(self):
        """
            This method returns the current Data Set
        """
        return self.validData

    def addElementToData(self,element):
        #TODO: make to model element and push it to the array
        self.validData.push(element)