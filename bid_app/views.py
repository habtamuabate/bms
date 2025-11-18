from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Bid

def dashboard(request):
    try:
        # Get counts safely
        total_projects = Project.objects.count()
        total_bids = Bid.objects.count()
        active_bids = Bid.objects.filter(status__in=['draft', 'submitted', 'under_review']).count()
        
        # Recent items
        recent_projects = Project.objects.all().order_by('-created_at')[:5]
        recent_bids = Bid.objects.all().order_by('-created_at')[:5]
        
        context = {
            'total_projects': total_projects,
            'total_bids': total_bids,
            'active_bids': active_bids,
            'upcoming_deadlines': 0,
            'recent_projects': recent_projects,
            'recent_bids': recent_bids,
        }
        return render(request, 'bid_app/dashboard.html', context)
    except Exception as e:
        # Fallback if there's any error
        print(f"Error in dashboard: {e}")  # This will show in console
        context = {
            'total_projects': 0,
            'total_bids': 0,
            'active_bids': 0,
            'upcoming_deadlines': 0,
            'recent_projects': [],
            'recent_bids': [],
        }
        return render(request, 'bid_app/dashboard.html', context)

def home(request):
    return HttpResponse("""
    <h1>Bid Management System</h1>
    <p>Server is working! <a href="/dashboard/">Go to Dashboard</a></p>
    <p><a href="/admin/">Admin Panel</a></p>
    <p><a href="/projects/">View Projects</a></p>
    <p><a href="/bids/">View Bids</a></p>
    """)

def project_list(request):
    try:
        projects = Project.objects.all()
        return render(request, 'bid_app/project_list.html', {'projects': projects})
    except Exception as e:
        print(f"Error in project_list: {e}")
        return render(request, 'bid_app/project_list.html', {'projects': []})

def bid_list(request):
    try:
        bids = Bid.objects.all()
        return render(request, 'bid_app/bid_list.html', {'bids': bids})
    except Exception as e:
        print(f"Error in bid_list: {e}")
        return render(request, 'bid_app/bid_list.html', {'bids': []})