from django.shortcuts import render

def tetris(request):
    return render(request, 'tetris/game.html')
    # return render(request, 'tetris/tetris.html')
