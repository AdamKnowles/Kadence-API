from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from kadence.models import Run
from datetime import datetime





class RunSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for a single instance of a run

    Arguments:
        serializers
    """

    class Meta:
        model = Run
        url = serializers.HyperlinkedIdentityField(
            view_name='runs',
            lookup_field='id'
        )
        fields = ('id', 'time', 'date', 'distance', 'duration')

        depth = 1


class Runs(ViewSet):
    

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized vital sign instance
        """
        new_run = Run()
        new_run.time = request.data["time"]
        new_run.date = request.data["date"]
        new_run.distance = request.data["distance"]
        new_run.duration = request.data["duration"]
        new_run.save()

        serializer = RunSerializer(new_run, context={'request': request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        

        
        try:
            
            run = Run.objects.get(pk=pk)
            serializer = RunSerializer(run, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    
    def list(self, request):
        

    # at the bottom, in the serializer, it returns all patients because "patients" is defined as "patient.objects.all()"
        runs = Run.objects.all()
        
        serializer = RunSerializer(
            runs, many=True, context={'request': request})
        return Response(serializer.data)

    

        