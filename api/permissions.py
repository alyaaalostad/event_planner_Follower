from rest_framework.permissions import BasePermission

class IsAttendee(BasePermission):
	message="You must be an attendee"

	def has_object_permission(self,request,view,obj):
		if request.user == obj.name:
			return True
		else:
			return False
			
class IsOwner(BasePermission):		# naming
	message="You must be the Event's Organizer"

	def has_object_permission(self,request,view,obj):
		if request.user == obj.organizer:
			return True
		else:
			return False