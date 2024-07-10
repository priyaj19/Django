from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

from rest_framework import status
from rest_framework.response import Response


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class AllMoviesListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    partial = True


class MovieDeleteView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Movie"))


# — `GET /api/tasks/` — List all tasks
# — `POST /api/tasks/` — Create a new task
# — `GET /api/tasks/{task_id}/` — Retrieve a specific task
# — `PUT /api/tasks/{task_id}/` — Update a specific task
# — `DELETE /api/tasks/{task_id}/` — Delete a specific taskAuthentication and
