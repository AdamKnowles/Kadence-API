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
        fields = ('id', 'time', 'date', 'distance', 'duration','got_after_it', 'pace', 'new_duration')

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
        new_run.got_after_it = request.data["got_after_it"]
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

    def destroy(self, request, pk=None):
        
        try:
            run = Run.objects.get(pk=pk)
            run.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Run.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def list(self, request):
        

    
        runs = Run.objects.all().order_by('date').reverse()
        
        serializer = RunSerializer(
            runs, many=True, context={'request': request})
        return Response(serializer.data)

        
    

        